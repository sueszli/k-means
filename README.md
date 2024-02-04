```
┌─────────────────────────────────┐
| do you know, what k even means? |
| ... because i still don't.      |
└─────────────────────────────────┘
    \
     \
      \       _.-.
         __.-' ,  \
        '--'-'._   \
                '.  \
                 )-- \ __.--._
                /   .'        '--.
               .               _/-._
               :       ____._/   _-'
               '._          _.'-'
                  '-._    _.'
                      \_|/
                     __|||
                     >__/'
```

<br>

_quick install:_

```bash
# clone
git clone https://github.com/sueszli/autodiff
cd autodiff

# install dependencies
if ! command -v python3 &>/dev/null; then echo "python3 is not installed."; return; fi
if ! command -v pip3 &>/dev/null; then echo "pip3 is not installed."; return; fi
python3 -m pip install --upgrade pip > /dev/null
pip3 install pipreqs > /dev/null && rm -rf requirements.txt > /dev/null && pipreqs . > /dev/null
pip3 install -r requirements.txt > /dev/null

# run
...

<< ////
...
////
```
