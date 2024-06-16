import tkinter as tk
import random


class FlappyBird:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Flappy Bird")

        self.canvas = tk.Canvas(self.window, width=400, height=600, bg='skyblue')
        self.canvas.pack()

        self.bird = self.canvas.create_oval(50, 250, 90, 290, fill='yellow')

        self.pipes = []
        self.create_pipes()

        self.window.bind('<space>', self.flap)

        self.gravity = 1
        self.flap_force = -15  # Adjusted flap force for better control
        self.bird_speed = 0

        self.score = 0
        self.score_text = self.canvas.create_text(200, 50, text='Score: 0', font=('Helvetica', 24), fill='white')

        self.update()
        self.window.mainloop()

    def create_pipes(self):
        gap = 200
        pipe_width = 100
        height = random.randint(150, 450)
        top_pipe = self.canvas.create_rectangle(400, 0, 400 + pipe_width, height, fill='green')
        bottom_pipe = self.canvas.create_rectangle(400, height + gap, 400 + pipe_width, 600, fill='green')
        self.pipes.append((top_pipe, bottom_pipe))

    def move_pipes(self):
        for pipe in self.pipes:
            self.canvas.move(pipe[0], -5, 0)
            self.canvas.move(pipe[1], -5, 0)
        if self.canvas.coords(self.pipes[0][0])[2] < 0:
            self.canvas.delete(self.pipes[0][0])
            self.canvas.delete(self.pipes[0][1])
            self.pipes.pop(0)
            self.create_pipes()
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f'Score: {self.score}')

    def flap(self, event):
        self.bird_speed = self.flap_force

    def update(self):
        self.bird_speed += self.gravity
        self.canvas.move(self.bird, 0, self.bird_speed)

        self.move_pipes()
        self.check_collision()

        self.window.after(20, self.update)

    def check_collision(self):
        bird_coords = self.canvas.coords(self.bird)
        if bird_coords[1] < 0 or bird_coords[3] > 600:
            self.game_over()

        for pipe in self.pipes:
            if self.canvas.coords(pipe[0])[2] > bird_coords[0] and self.canvas.coords(pipe[0])[0] < bird_coords[2]:
                if bird_coords[1] < self.canvas.coords(pipe[0])[3] or bird_coords[3] > self.canvas.coords(pipe[1])[1]:
                    self.game_over()

    def game_over(self):
        self.canvas.create_text(200, 300, text='Game Over', font=('Helvetica', 36), fill='red')
        self.window.update()
        self.window.after(2000, self.window.destroy)


if __name__ == "__main__":
    FlappyBird()
