```
┌───────────────────────────────────────────────┐
| honestly, i still don't know what k means ... |
└───────────────────────────────────────────────┘
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
git clone https://github.com/sueszli/k-means
cd k-means

# install dependencies
if ! command -v python3 &>/dev/null; then echo "python3 is not installed."; return; fi
if ! command -v pip3 &>/dev/null; then echo "pip3 is not installed."; return; fi
python3 -m pip install --upgrade pip
pip3 install pipreqs && rm -rf requirements.txt && pipreqs .
pip3 install -r requirements.txt

# run
python3 k-means.py


<< ////
...
////
```
