from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A/%B/%Y')
    print(data_atual)
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=11, minute=7, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(horario_str)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.weekday())
    tupla_day = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    tupla_month = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print(tupla_day[data_atual.weekday()])
    print(tupla_month[data_atual.month - 1])
    data_criada = datetime(2000, 12, 20, 15, 15, 2)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:34:09'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)


if __name__ == '__main__':
    trabalhando_com_date()
    # trabalhando_com_time()
    # trabalhando_com_datetime()