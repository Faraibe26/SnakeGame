# SnakeGame


# 🐍 Snake Game (Turtle Edition)

A classic **Snake game** built in Python using the `turtle` graphics module. Eat food to grow your snake and avoid crashing into yourself. This version includes **blinking food**, **animated snake movement**, and intuitive arrow-key controls!

---

## 🚀 How to Run the Game

1. **Make sure you have Python 3 installed** on your machine.
2. This game uses the built-in `turtle` and `time` modules, so no additional installations are required.
3. Run the game using this command:
   ```bash
   python main.py
   ```

---

## 🎮 Controls

- Use the **Arrow Keys** to move the snake:
  - `↑` Up
  - `↓` Down
  - `←` Left
  - `→` Right

---

## 🧠 Features

- Smooth movement and redraw using `ontimer()`
- Food that **blinks** every few frames
- Snake **grows** when it eats food
- Basic **collision detection**
- Organized with OOP:
  - `Square` – represents each part of the snake’s body
  - `Food` – blinking food square that changes location
  - `Snake` – manages movement, growth, and drawing
  - `Game` – ties all components together and handles the game loop

---

## 🔧 File Structure

- `main.py` – Full source code, encapsulated with classes: `Square`, `Food`, `Snake`, `Game`

---

## 🧪 Future Improvements

- Better collision detection with game-over logic
- Score tracking
- Walls and boundaries
- Difficulty modes (speed increase over time)

---

## 📷 Preview

The game opens in a new window and looks like a retro-style square-grid Snake game with blinking food. The snake grows as it eats, and you can control it using the arrow keys.

---
