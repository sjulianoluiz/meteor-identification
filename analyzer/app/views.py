from django.shortcuts import render,redirect

def index(request):
  return render(request, "principal.html")

def duvidosos(request):
  return render(request, "duvidosos.html")

def finalizar(request):
  return render(request, "finalizar.html")

def configuracoes(request):
  if request.POST:

    return render(request, 'configuracoes.html', {'imagem': 1})      
  else:
    return render(request, 'configuracoes.html')
