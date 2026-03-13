# 🏭 Factory Design Pattern — Python

A clean Python implementation of the **Factory Design Pattern** across two tasks, demonstrating how to decouple object creation from client code using ABC-enforced interfaces.

---

## 📌 What is the Factory Pattern?

The **Factory Pattern** is a creational design pattern that provides a **centralized way to create objects** without exposing the instantiation logic to the client. Instead of calling constructors directly, the client asks a factory to return the right object based on input.

> Create objects without specifying the exact class to instantiate.

---

## ⚙️ How It Works

### Task 1 — Page Factory

A `PageFactory` takes a string input and returns the corresponding page object. All pages implement the `Page` abstract interface, guaranteeing they expose a `display()` method.

```
"home"    →  HomePage()
"contact" →  ContactPage()
"about"   →  AboutPage()
```

### Task 02 — Popup Factory

A `PopupFactory` takes a string input and returns the corresponding popup object. All popups implement the `Popup` abstract interface, guaranteeing they expose a `show()` method.

---

## 🧠 Key OOP Concepts Used

- **Abstraction** — `Page` and `Popup` define contracts via `ABC`
- **Polymorphism** — all products are interchangeable under their interface
- **Encapsulation** — object creation logic is hidden inside the factory
- **Single Responsibility** — each class has one job

---

## 🐍 Requirements

- Python 3.x
- No external libraries needed

---

## 👤 Author

**Muhammad Abdullah**  
