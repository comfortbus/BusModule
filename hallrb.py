import RPIO

pinHallin = 4 # pino do sensor Hall entrada (número GPIO)
pinHallout = 5 # pino do sensor Hall saída
inputValuein = 0 # valor lido
inputValueout = 0;
i = 0; # contador entrada
o = 0; # contador saída
t = 0; # contador total 

RPIO.setup(pinHallin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(pinHallout, RPIO.IN, pull_up_down=RPIO.PUD_UP)

while (True):
  # enquanto o sensor não passar continuar
  # lendo a entrada, depois que ele entra
  # inputValue vai para 0 e ele sai do laço
  while(inputValuein | inputValueout):
	inputValuein = RPIO.input(pinHallin)
	inputValueout = RPIO.input(pinHallout)
  
  if (inputValuein):
    i = i + 1
    print("Contagem de Entrada:")
    print(i)
  
  if (inputValueout):
    o = o + 1
    print("Contagem de Saída:")
    print(o)
  
  t = i - o
  print(t)
  
  inputValuein = True
  inputValueout = True
