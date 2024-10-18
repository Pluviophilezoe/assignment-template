import streamlit as st
import pygame
from image_generator import generate_image

def console_mode():
    width = int(input("请输入图像宽度: "))
    height = int(input("请输入图像高度: "))
    
    img = generate_image(width, height)
    img.show()

def web_ui():
    st.title("AI 图片生成器")

    width = st.slider("图像宽度", 100, 800, 400)
    height = st.slider("图像高度", 100, 800, 400)

    if st.button("生成图像"):
        img = generate_image(width, height)
        st.image(img, caption="生成的图像")

def pygame_mode():
    pygame.init()
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("AI 图片生成器")

    img = generate_image(width, height)
    mode = img.mode
    size = img.size
    data = img.tobytes()

    image = pygame.image.fromstring(data, size, mode)
    screen.blit(image, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    img = generate_image(width, height)
                    data = img.tobytes()
                    image = pygame.image.fromstring(data, size, mode)
                    screen.blit(image, (0, 0))
                    pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    mode = input("选择模式 (console/web/pygame): ").strip().lower()
    if mode == "console":
        console_mode()
    elif mode == "web":
        web_ui()
    elif mode == "pygame":
        pygame_mode()
    else:
        print("无效模式，请选择 'console', 'web', 或 'pygame'.")