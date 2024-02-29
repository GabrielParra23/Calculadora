
import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    )

#passo a passo

#2 passo: criar os botoes
class CalculatorApp(UserControl):
    def build(self):
        self.reset()
        self.resultado = Text(value = "0", color="white", size=20)
        
        return Container(
            padding=20,
            border_radius=border_radius.all(20),
            bgcolor= colors.BLACK,
            width=300,
            content=Column(
                
                controls=[
                    Row(controls=[self.resultado], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                expand=1,
                                on_click= self.botao,
                                data="AC",
                            ),
                            ElevatedButton(
                                text="+/-",
                                expand=1,
                                data="+/-",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="%",
                                expand=1,
                                data="%",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="/",
                                expand=1,
                                bgcolor="green",
                                data="/",
                                on_click= self.botao,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                expand=1,
                                data="7",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="8",
                                expand=1,
                                data="8",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="9",
                                expand=1,
                                data="9",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="*",
                                expand=1,
                                bgcolor="green",
                                data="*",
                                on_click= self.botao,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                expand=1,
                                data="4",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="5",
                                expand=1,
                                data="5",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="6",
                                expand=1,
                                data="6",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="-",
                                expand=1,
                                bgcolor="green",
                                data="-",
                                on_click= self.botao,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                expand=1,
                                data="1",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="2",
                                expand=1,
                                data="2",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="3",
                                expand=1,
                                data="3",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="+",
                                expand=1,
                                bgcolor="green",
                                data="+",
                                on_click= self.botao,
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                expand=1,
                                data="0",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text=".",
                                expand=1,
                                data=".",
                                on_click= self.botao,
                            ),
                            ElevatedButton(
                                text="=",
                                expand=1,
                                bgcolor="orange",
                                data="=",
                                on_click= self.botao,
                            ),
                        ]
                    ),
            
                ]
                
                
            ),
                    
        )
    #3 passo: dar funcionalidade aos botoes
    
    
   
    
    def botao(self, e):
        data = e.control.data
        if self.resultado.value == "Erro" or data == "AC":
            self.resultado.value = "0"
            self.reset()
            
            
         #dando funcionalidade aos numeros   
        elif data in ("1","2","3","4","5","6","7","8","9","0","."):
            if self.resultado.value == "0" or self.nova_operacao == True:
                self.resultado.value = data
                self.nova_operacao = False
                
                
            else: 
                self.resultado.value = self.resultado.value + data
                
                
        # dando funcionalidade as funções       
        elif data in ("/","*","-","+"):
            self.resultado.value = self.calculo( 
                self.operacao1, float(self.resultado.value), self.operador
            )
            #caso a operação 1 não seja 0 ou o resultado seja erro então a operação 1 ira pegar o numero do resultado para ele e transformar a nova operação em verdadeiro para que seja possivel colocar a nova operação;
            self.operador = data 
            if self.resultado.value == "Erro":
                self.operacao1 = "0"
            
            else:
                self.operacao1 = float(self.resultado.value)
            self.nova_operacao = True
                
        elif data in ("="):
            self.resultado.value = self.calculo(
                self.operacao1,
                float(self.resultado.value),
                self.operador
            )
            self.reset()
            
        elif data in ('%'):
            self.resultado.value = float(self.resultado.value) / 100
            self.reset
            
        elif data in ("+/-"):
            if float(self.resultado.value) > 0:
                self.resultado.value = "-" + str(self.resultado.value)
            
            elif float(self.resultado.value) < 0:
                self.resultado.value = str(
                    self.formatar_numero(abs(float(self.resultado.value)))
                )
        self.update()
    #operações
    def formatar_numero(self, num):
        if num %1 == 0:
            return int(num)
        else:
            return num
               
    def calculo(self, operacao1, operacao2, operador):
        if operador == "+":
            return self.formatar_numero (operacao1 + operacao2)
            
        elif operador == "*":
            return self.formatar_numero (operacao1 * operacao2) 
            
        elif operador == "-":
            return self.formatar_numero (operacao1 - operacao2)
        elif operador == "/":
            if operacao2 ==  0:
                return "Erro"
            else:
                return self.formatar_numero (operacao1 / operacao2) 
    
    
    
    def reset(self):
        self.operador = "+"
        self.operacao1 = 0
        self.nova_operacao = True
            

#1 passo: criar a pagina inicial

def main(pagina: ft.Page):
    pagina.title = "Calculadora"
    
    
    calc = CalculatorApp()
    
    pagina.add(calc)
    
ft.app(target=main)
    
    
    
    
        
    
            
            
        
    
    
    
    
      
    
    
    
   
ft.app(target=main)  
    
    

    
    
        
  
    

  