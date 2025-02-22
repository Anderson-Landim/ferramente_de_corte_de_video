from moviepy import VideoFileClip
import os

def dividir_video(video_path, output_folder="output_videos", segment_duration=90):
    # Criar a pasta de saída, se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Carregar o vídeo
    video = VideoFileClip(video_path)
    total_duration = int(video.duration)  # Duração total do vídeo

    # Criar os segmentos de 90 segundos
    for i, start_time in enumerate(range(0, total_duration, segment_duration)):
        end_time = min(start_time + segment_duration, total_duration)  # Garante que não passe do final do vídeo
        clip = video.subclipped(start_time, end_time)
        output_path = os.path.join(output_folder, f"parte_{i+1}.mp4")
        clip.write_videofile(output_path, codec="libx264", fps=30)

    print(f"✅ Vídeo dividido em partes de {segment_duration} segundos. Arquivos salvos em: {output_folder}")

# Exemplo de uso
video_path = "segundo.mp4"  # Substitua pelo caminho do vídeo
dividir_video(video_path)
