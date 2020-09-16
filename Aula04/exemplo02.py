for fn in uploaded.keys():
  print('Arquivo "{name}" com tamanho de {length} bytes'.format(
      name=fn, length=len(uploaded[fn])
  ))