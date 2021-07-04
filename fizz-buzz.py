class FizzBuzz:

    __rules = [
        {
            'multiple':3,
            'word':['fizz']
        },
        {
            'multiple':5,
            'word':['buzz']
        }
    ]

    def __init__(self, start=1, end=100):
        self.startCount = start
        self.endCount = end
        return

    def __isMult(self, num, mult):
        return (num % mult == 0)

    def play(self):
        for i in range(self.startCount, self.endCount):
            output = ''
            for rule in self.__rules:
                if self.__isMult(i, rule['multiple']):
                    for word in rule['word']:
                        output += word
            if output == '':
                print(i)
            else:
                print(output)
        print(self.__rules)

    def getRule(self, key, value):
        for rule in self.__rules:
            try:
                ruleToReturn = rule if value in rule[key] else None
            except TypeError as err:
                print(err)
                ruleToReturn = rule if rule[key] == value else None
                print(f'ruleKey {rule[key]}')
                print(f'ruleToReturn {ruleToReturn}')
            except:
                print('final except')
                ruleToReturn = None
            finally:
                if ruleToReturn:
                    break

        return ruleToReturn
            
    def addRule(self, multiple, word):
        rule = self.getRule('multiple', multiple)
        if rule and word in rule['word']:
            return
        if rule:
            rule['word'] += [word]
            return
        self.__rules.append({
            'multiple':multiple,
            'word':[word]
        })

    def deleteRule(self, multiple, word):
        rule = self.getRule('multiple', multiple)
        if not rule:
            print('deleteRule rule is None')
            return
        if word in rule['word']:
            rule['word'].remove(word)
        if len(rule['word']) == 0:
            self.__rules.remove(rule)
        return
            

game = FizzBuzz()
game.play()
game.addRule(4, 'pop')
game.play()
game.deleteRule(3, 'fizz')
game.play()
game.addRule(4, 'bang')
game.play()