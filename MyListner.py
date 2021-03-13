import regex as regex

from com.antlr.grammarBuchnevIlyaListener import grammarBuchnevIlyaListener
from com.antlr.grammarBuchnevIlyaParser import grammarBuchnevIlyaParser


class MyGrammarListner(grammarBuchnevIlyaListener):

    def enterProgram(self, ctx: grammarBuchnevIlyaParser.ProgramContext):
        self.variables = {}
        self.stack_value = []

    def enterDescription(self, ctx: grammarBuchnevIlyaParser.DescriptionContext):
        # проходимся циклом по токенам до :
        type = ctx.TYPE()[0]
        for identifier in ctx.IDENTIFIER():
            self.variables[identifier.__str__()] = {
                'type': type.__str__(),
                'value': 'None'
            }

    def exitDescription(self, ctx: grammarBuchnevIlyaParser.DescriptionContext):
        pass

    def enterExpression(self, ctx: grammarBuchnevIlyaParser.ExpressionContext):
        pass

    def exitExpression(self, ctx: grammarBuchnevIlyaParser.ExpressionContext):
        pass

    def exitAssignments(self, ctx: grammarBuchnevIlyaParser.AssignmentsContext):
        # Присваивание
        buf_ident = ctx.IDENTIFIER().__str__()
        if buf_ident in self.variables.keys():
            # проверяем на типы данных
            # expression - должен быть последним в наборе данных, по этому берем последнее
            expression = self.stack_value[-1]
            if self.variables[buf_ident]['type'] == expression['type']:
                self.variables[buf_ident]['value'] = expression['value']
                #print(str(buf_ident) + ' = ' + str(self.variables[buf_ident]['value']))
            elif self.variables[buf_ident]['type'] == '%' and expression['type'] == '!':
                self.variables[buf_ident]['type'] ='!'
                self.variables[buf_ident]['value'] = expression['value']
            elif self.variables[buf_ident]['type'] == '!' and expression['type'] == '%':
                self.variables[buf_ident]['value'] = expression['value']
            else:
                print('Ошибка! Переменной ' + self.variables[buf_ident]['type']+ ' нельзя присвоить данные типа ' + expression['type'])
        print(str(buf_ident) + ' = ' + str(self.variables[buf_ident]['value']))

    def exitExpression(self, ctx: grammarBuchnevIlyaParser.ExpressionContext):
        if ctx.OPERATION_RELATIONSHIP():
            print(ctx.OPERATION_RELATIONSHIP())
        return

    def exitOperand(self, ctx: grammarBuchnevIlyaParser.OperandContext):
        if ctx.OPERATION_SUMMARY():
            count_move = len(ctx.OPERATION_SUMMARY())
            list_operand = list(reversed(self.stack_value[-(count_move+1):]))
            del self.stack_value[-(count_move + 1):]
            for i in range(0, len(ctx.OPERATION_SUMMARY())):
                buf_value = {'type': None, 'value': None}
                operation = str(ctx.OPERATION_SUMMARY()[i])
                left = list_operand[count_move-i]
                right = list_operand[count_move-i-1]
                if operation == '+':
                    if left['type'] != '$' and right['type'] != '$':
                        buf_value['value'] = left['value'] + right['value']
                        # TODO
                        if left['type'] == '!' or right['type'] == '!':
                            buf_value['type'] = '!'
                        else:
                            buf_value['type'] = '%'
                elif operation == '-':
                    if left['type'] != '$' and right['type'] != '$':
                        buf_value['value'] = left['value'] - right['value']
                        if left['type'] == '!' or right['type'] == '!':
                            buf_value['type'] = '!'
                        else:
                            buf_value['type'] = '%'
                elif operation == 'or':
                    if left['type'] == '$' and right['type'] == '$':
                        buf_value = left['value'] | right['value']
                del list_operand[count_move - i]
                del list_operand[count_move - i - 1]
                list_operand.append({'type': buf_value['type'], 'value': buf_value['value']})
            self.stack_value.append(list_operand[0])
            #print('exit operand')

    def exitSummand(self, ctx: grammarBuchnevIlyaParser.SummandContext):
        if ctx.OPERATION_MULTIPLE():
            count_move = len(ctx.OPERATION_MULTIPLE())
            list_operand = list(reversed(self.stack_value[-(count_move + 1):]))
            del self.stack_value[-(count_move + 1):]
            for i in range(0, len(ctx.OPERATION_MULTIPLE())):
                buf_value = {'type': None, 'value': None}
                operation = str(ctx.OPERATION_MULTIPLE()[i])
                left = list_operand[count_move - i]
                right = list_operand[count_move - i - 1]
                if operation == '*':
                    if left['type'] != '$' and right['type'] != '$':
                        buf_value['value'] = left['value'] * right['value']
                        if left['type'] == '!' or right['type'] == '!':
                            buf_value['type'] = '!'
                        else:
                            buf_value['type'] = '%'
                elif operation == '/':
                    if left['type'] != '$' and right['type'] != '$':
                        buf_value['value'] = left['value'] / right['value']
                        buf_value['type'] = '!'#float
                elif operation == 'and':
                    if left['type'] == '$' and right['type'] == '$':
                        buf_value = left['value'] & right['value']
                del list_operand[count_move - i]
                del list_operand[count_move - i - 1]
                list_operand.append({'type': buf_value['type'], 'value': buf_value['value']})
            self.stack_value.append(list_operand[0])
            #print('exit operand')
        #print('exit summand')

    def exitMultiplier(self, ctx: grammarBuchnevIlyaParser.MultiplierContext):
        #Здесь необходимо записать данные о значении просто в память
        if ctx.BOOL():
            self.stack_value.append(self.get_value_with_type(ctx.BOOL()))
        elif ctx.IDENTIFIER():
            self.stack_value.append(self.variables[str(ctx.IDENTIFIER())])
        elif ctx.NUMBERS():
            self.stack_value.append(self.get_value_with_type(ctx.NUMBERS().__str__()))
        elif ctx.OPERATION_UNARY():
            # TODO Доделать
            self.stack_value.append('~')
        elif ctx.BLOCK_OPEN() and ctx.BLOCK_CLOSE():
            #TODO Доделать
            self.stack_value.append(ctx.BLOCK_OPEN().__str__())
            self.stack_value.append(ctx.BLOCK_CLOSE().__str__())
        #print('exit multiplier')

    def exitProgram(self, ctx: grammarBuchnevIlyaParser.ProgramContext):
        print('Программа закончила свою работу')

    def exitOutput_m(self, ctx:grammarBuchnevIlyaParser.Output_mContext):
        list_children = [ x for x in ctx.children if str(x) not in ['output','(',')']]
        buf_k = ''
        for x in list_children:
            try:
                buf_k += str(self.get_value_with_type(x.start.text))
            except:
                buf_k += str(self.get_value_with_type(x.symbol.text))
            buf_k += '\n'
        print(buf_k)

    def get_value_with_type(self, value: str) -> dict:
        output = {
            'type': None,
            'value': None
        }
        if value in self.variables.keys():
            return self.variables[value]
        # если bool
        if any(x in value for x in ['true', 'false']):
            output['type'] = '$'
            if value == 'true':
                output['value'] = True
            else:
                output['value'] = False
        # если real
        # < действительное >: := < числовая_строка > < порядок > | [ < числовая_строка >].< числовая_строка > [
        #   порядок]
        elif regex.fullmatch(r'([0-9]+[eE][+-][0-9]+)|([0-9]*\.[0-9]+([eE][+-][0-9]+)?)', value):
            output['type'] = '!'
            output['value'] = float(value)
        else:
            output['type'] = '%'
            # двоичное
            if regex.fullmatch(r'[01]+[bB]', value):
                value = regex.split(r'[bB]',value)[0]
                output['value'] = int(value, 2)
            # восьмиричное
            elif regex.fullmatch(r'[0-7]+[oO]', value):
                value = regex.split(r'[oO]',value)[0]
                output['value'] = int(value, 8)
            # десятичное
            elif regex.fullmatch(r'[0-9]+[dD]?', value):
                value = regex.split(r'[dD]', value)[0]
                output['value'] = int(value, 10)
            # шестнадцатеричное
            elif regex.fullmatch(r'[0-9][0-9a-fA-F]+[hH]', value):
                value = regex.split(r'[hH]', value)[0]
                output['value'] = int(value, 16)

        return output
