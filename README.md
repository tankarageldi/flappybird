# Flappy Bird AI with Neural Network

## Overview

This project implements an AI-powered Flappy Bird game using a Perceptron-based Neural Network. The AI learns to play Flappy Bird through natural selection and a fitness-based evaluation system.

## Features

- **Perceptron Neural Network**: The AI uses a simple neural network with input nodes representing the bird's vision and an output determining its jump decision.
- **Natural Selection**: The AI evolves over multiple generations using a genetic algorithm to improve performance.
- **Fitness Score**: The survival time of each bird determines its fitness, influencing the next generation's selection.
- **Species Classification**: Birds are grouped into species based on weight differences in their neural networks.
- **Dynamic Gameplay**: Pipes spawn dynamically, and the AI continuously learns from previous attempts.

## Project Structure

```bash
flappybird/

│── main.py           # Main game loop
│── img/              # visualization images for pipes and birds.
│── src/
    │── config.py         # Game configurations (window size, pipes, etc.)
    │── components.py     # Game elements (ground, pipes)
    │── player.py        # Player class representing the AI bird
    │── population.py    # Handles natural selection and species classification
    │── species.py       # Manages species grouping
    │── brain.py         # Neural network for decision-making
    │── connection.py    # Handles connections between neural network nodes
    │── node.py          # Defines individual neural network nodes
```

## Installation

Ensure you have Python installed along with the required dependencies:

```bash
pip install pygame
```

## How to Run

Navigate to the project directory and execute:

```bash
python main.py
```

## How It Works

1. **Game Initialization**: The game window opens, and a population of birds (AI players) is created.
2. **AI Perception**: Each bird observes its environment using three vision inputs:
   - Distance to the top pipe
   - Horizontal distance to the pipe
   - Distance to the bottom pipe
3. **Decision Making**: The AI's neural network processes inputs and decides whether to jump.
4. **Survival and Fitness Calculation**: Birds that survive longer score higher fitness points.
5. **Natural Selection**: After all birds perish, the fittest individuals reproduce to create the next generation.
6. **Species Grouping**: Birds with similar neural weights are grouped into species.
7. **Mutation and Evolution**: Random mutations occur in the offspring, allowing the AI to evolve over time.

