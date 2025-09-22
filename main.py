from PIL import Image
import os

def extract_frames_from_gif(gif_path, output_folder="frames"):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开 GIF 文件
    with Image.open(gif_path) as gif:
        frame = 0
        while True:
            # 保存当前帧为 PNG
            frame_path = os.path.join(output_folder,"gif16", f"frame_{frame:03d}.png")
            gif.save(frame_path, format="PNG")
            frame += 1

            # 尝试跳到下一帧
            try:
                gif.seek(gif.tell() + 1)
            except EOFError:
                break  # 没有更多帧，退出循环

    print(f"已将 {frame} 帧保存到 '{output_folder}' 文件夹中。")

# ========== 主程序 ==========
if __name__ == "__main__":
    gif_path = "16.gif"  # 替换为你的 GIF 路径
    extract_frames_from_gif(gif_path)
