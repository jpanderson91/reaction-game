from pyfiglet import figlet_format
from colorama import Fore, Back, Style

def side_by_side(left, right, spacing=4):
    left_lines = left.splitlines()
    right_lines = right.splitlines()
    left_width = max(len(line) for line in left_lines)
    max_lines = max(len(left_lines), len(right_lines))
    result = []
    for i in range(max_lines):
        l = left_lines[i] if i < len(left_lines) else ""
        r = right_lines[i] if i < len(right_lines) else ""
        result.append(f"{l:<{left_width}}{' ' * spacing}{r}")
    return "\n".join(result)


WELCOME_ART = r"""
                                |     |
                                \\_V_//
                                \/=|=\/
                                 [=v=]
                               __\___/_____
                              /..[  _____  ]
                             /_  [ [  M /] ]
                            /../.[ [ M /@] ]
                           <-->[_[ [M /@/] ]
                          /../ [.[ [ /@/ ] ]
     _________________]\ /__/  [_[ [/@/ C] ]
    <_________________>>0---]  [=\ \@/ C / /
       ___      ___   ]/000o   /__\ \ C / /
          \    /              /....\ \_/ /
       ....\||/....           [___/=\___/
      .    .  .    .          [...] [...]
     .      ..      .         [___/ \___]
     .    0 .. 0    .         <---> <--->
  /\/\.    .  .    ./\/\      [..]   [..]
 / / / .../|  |\... \ \ \    _[__]   [__]_
/ / /       \/       \ \ \  [____>   <____]
"""

def print_banner(text="Incident Response"):
    print(Fore.GREEN)
    print(side_by_side(WELCOME_ART, figlet_format(text)))
    print(Style.RESET_ALL)