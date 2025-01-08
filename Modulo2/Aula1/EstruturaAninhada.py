anos_experiencia = int(input("Quantos anos de experiência você tem? "))

if anos_experiencia == 0:
    nivel = 'Estagiário'
elif anos_experiencia <= 3:
    nivel = 'Junior'
elif anos_experiencia <= 8:
      nivel = 'Pleno'
else:
    nivel = 'Sênior'

print(f"Você é um {nivel}")
    
    
    