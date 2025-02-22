Aqui está uma descrição para o seu repositório no GitHub:  

---

# 🎬 Divisor de Vídeos com MoviePy  

Este script em Python permite dividir vídeos em segmentos de duração personalizada utilizando a biblioteca **MoviePy**.  

## 🚀 Funcionalidades  
✅ Divide vídeos automaticamente em partes de duração definida (padrão: 90 segundos)  
✅ Salva os arquivos de saída em uma pasta específica  
✅ Mantém a qualidade do vídeo com o codec **libx264**  

## 🛠️ Como Usar  

1️⃣ Instale as dependências necessárias:  
```bash
pip install moviepy
```

2️⃣ Execute o script passando o caminho do vídeo:  
```python
video_path = "meu_video.mp4"  # Substitua pelo seu vídeo
dividir_video(video_path)
```

Os vídeos divididos serão salvos na pasta **output_videos**.  

## 📌 Observação  
- O tempo de segmentação pode ser ajustado modificando o parâmetro `segment_duration`.  
- Certifique-se de que o **MoviePy** e seus codecs estejam corretamente configurados.  

📩 Sinta-se à vontade para contribuir ou relatar problemas! 🚀🎥
