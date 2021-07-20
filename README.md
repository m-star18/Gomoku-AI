# Gomoku-AI

[![Github issues](https://img.shields.io/github/issues/m-star18/Gomoku-AI)](https://github.com/m-star18/Gomoku-AI/issues)
[![Github stars](https://img.shields.io/github/stars/m-star18/Gomoku-AI)](https://github.com/m-star18/Gomoku-AI/stargazers)
[![Github top language](https://img.shields.io/github/languages/top/m-star18/Gomoku-AI)](https://github.com/m-star18/Gomoku-AI/)
[![Github license](https://img.shields.io/github/license/m-star18/Gomoku-AI)](https://github.com/m-star18/Gomoku-AI/)

![playout400](https://raw.githubusercontent.com/junxiaosong/AlphaZero_Gomoku/master/playout400.gif)

This is an implementation of the AlphaZero algorithm for playing the simple board game Gomoku (also called Gobang or Five in a Row) from pure self-play training. The game Gomoku is much simpler than Go or chess, so that we can focus on the training scheme of AlphaZero and obtain a pretty good AI model on a single PC in a few hours. 

## Prerequisites

- Python 3.9
- Numpy 1.21.1
- Pytorch 1.9.0

## Getting Started

To play with provided models, run the following script from the directory:  
```
python src/env/human_play.py  
```
You may modify human_play.py to try different provided models or the pure MCTS.

To train the AI model from scratch, directly run:   
```
python src/train.py
```

## License

This program is released under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
