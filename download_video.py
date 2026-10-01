from pytubefix import YouTube
from pytubefix.cli import on_progress
import subprocess
import os
import re

def clean_filename(filename):
    """清理文件名中的非法字符"""
    # 替换特殊字符为下划线
    clean = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return clean.strip()

def download_and_merge(url):
    try:
        print(f"\n正在获取视频信息...")
        yt = YouTube(url, on_progress_callback=on_progress)
        
        print(f"\n📹 视频标题：{yt.title}")
        print(f" 时长：{yt.length // 60}分{yt.length % 60}秒")
        
        # 获取最高清视频流
        video_stream = yt.streams.filter(type='video').order_by('resolution').desc().first()
        audio_stream = yt.streams.filter(only_audio=True).order_by('bitrate').desc().first()
        
        if not video_stream or not audio_stream:
            print("\n 未找到可下载的视频流或音频流")
            return False
        
        print(f"\n 视频: {video_stream}")
        print(f" 音频: {audio_stream}")
        
        # 创建安全的文件名
        base_name = clean_filename(yt.title)[:100]  # 限制长度防止过长
        video_temp = f"{base_name}_video.mp4"
        audio_temp = f"{base_name}_audio.m4a"
        final_file = f"{base_name}_final.mp4"
        
        # 下载视频
        print(f"\n⏳ 正在下载视频 (2160p 60fps)...")
        video_stream.download(filename=video_temp)
        
        # 下载音频
        print(f"⏳ 正在下载音频 (160kbps)...")
        audio_stream.download(filename=audio_temp)
        
        print(f" 音视频下载完成!")
        
        # 检查 ffmpeg
        try:
            subprocess.run(
                ['ffmpeg', '-version'],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                check=True
            )
        except:
            print("\n 未找到 ffmpeg，请先安装：winget install ffmpeg")
            return False
        
        # 合并音视频
        print(f"\n🔗 正在合并音视频 (可能需要几分钟)...")
        result = subprocess.run([
            'ffmpeg', '-y',
            '-i', video_temp,
            '-i', audio_temp,
            '-c:v', 'copy',
            '-c:a', 'copy',
            final_file
        ], capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        if result.returncode == 0:
            print(f"\n 合并成功!")
            print(f" 文件位置：{os.path.abspath(final_file)}")
            
            # 删除临时文件
            os.remove(video_temp)
            os.remove(audio_temp)
            print(f"🗑️  已清理临时文件")
            return True
        else:
            print(f"\n 合并失败：{result.stderr[:200]}")
            return False
            
    except Exception as e:
        print(f"\n 发生错误：{e}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("         Batube 视频自动下载工具 基础版")
    print("         支持最高画质 + 自动合并音视频")
    print("="*60)

    # 循环下载
    while True:
        url = input("\n请输入 YouTube 视频链接 (或输入 q 退出):\n> ").strip()
        
        if url.lower() == 'q':
            print("再见！")
            break
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        success = download_and_merge(url)
        
        print("\n" + "="*60)
        if success:
            print("任务完成！文件已保存到当前目录")
        else:
            print("下载失败，请检查错误或重试")
        print("="*60)
