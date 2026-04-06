# Wythoff's Game #

## Clone enviornemnt ## 

```
git clone https://github.com/LazarPajic/Math302-Wythoff-s-Game.git
```

## Setting up Virtual Enviornment ## 

Use the command in bash to create a new enviornment (this only has to be done once)

``` 
python -m venv venv
```

Activate enviornment using bash command

```
source venv/bin/activate
```

Install required libraries

```
pip install -r requirements.txt 
```

You may have to update pip first

```
pip install --upgrade pip
```

Run Demo

```
python demo.py
```

Visualize the convergence to the golden ratio

```
python plot_convergence.py
```

Play the game using a GUI

```
python gui.py
```

Play the game using the terminal

```
python cli.py
```

Note: Replace python with the version you use to run python scripts (ie python3, py ...)
