from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class floating(FloatLayout):
    def find(self):
        #button functionality
        name = self.ids.name.text
        crush = self.ids.crush.text

        #copy of the names for display
        name_copy = self.ids.name.text
        crush_copy = self.ids.crush.text
    
        #self.add_widget(Label(text = f'{name}, {crush}'))  
    
        #making the names as a list of characters
        name = name.strip().lower().replace(" ","")
        crush = crush.strip().lower().replace(" ","")
        name = [*name]
        crush = [*crush]

        #removing the same words on both name
        count = 0
        for i in name:
            for j in crush:
                if i == j:
                    crush.remove(j)
                    count += 1
                    break
        total_length = (len(name)+len(crush)) - count

        #FLAMES logic
        count = 0
        lis = 'flames'
        i = 0
        count1 = 0

        while count1 < 1:
            if i == len(lis):
                i = 0
            if lis[i] != '1':
                count += 1
            if count == total_length:
                value = lis[i]
                lis = lis.replace(value,'1')
                count = 0
                for j in lis:
                    if j != '1':
                        count1 += 1
            if count1 == 1:
                for char in lis:
                    if char != '1':
                        if char == 'f':
                            return self.add_widget(Label(text = f'We found that {name_copy} and {crush_copy} will end up as "Friends"',valign =  'bottom',halign = 'center',text_size = (self.width-50 ,self.height-250),font_size = '25sp',color = 'FFD700'))
                        elif char == 'l':
                            return self.add_widget(Label(text = f'We found that {name_copy} and {crush_copy} will end as "Lovers"',valign =  'bottom',halign = 'center',text_size = (self.width-50 ,self.height-250),font_size = '25sp',color = 'FFD700'))
                        elif char == 'a':
                            return self.add_widget(Label(text = f'We found that {name_copy} and {crush_copy} will end up as "Affection"',valign =  'bottom',halign = 'center',text_size = (self.width-50 ,self.height-250),font_size = '25sp',color = 'FFD700'))
                        elif char == 'm':
                            return self.add_widget(Label(text = f'We found that {name_copy} and {crush_copy} will end up in "Marriage"',valign =  'bottom',halign = 'center',text_size = (self.width-50 ,self.height-250),font_size = '25sp',color = 'FFD700'))
                        elif char == 'e':
                            return self.add_widget(Label(text = f'We found that {name_copy} and {crush_copy} are "Enemies"',valign =  'bottom',halign = 'center',text_size = (self.width-50 ,self.height-250),font_size = '25sp',color = 'FFD700'))
                        elif char == 's':
                            return self.add_widget(Label(text = f'We found that {crush_copy} will end up as a "Sister/Brother" for you',valign =  'bottom',halign = 'center',text_size = (self.width-50 ,self.height-250),font_size = '25sp',color = 'FFD700'))
            else:
                count1 = 0
            i += 1 

class Fl(App):
    def build(self):
        return floating()

if __name__ == '__main__':
    Fl().run()