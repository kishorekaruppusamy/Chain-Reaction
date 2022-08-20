from flask import *

app = Flask(__name__)
from Game import *


# Starting route
@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        value = request.form['button']
        msg = request.form['choice']
        row, col = mapper(int(value))
        if msg == 'red':
            msg = red_play(row, col)
        elif msg == 'red_start':
            msg = red_play_first(row, col)
        else:
            msg = green_play(row, col)
        Star_Converter()
        return render_template('index.html', Display_Box=Display_Box, board_Player=board_Player, msg=msg)

    else:
        return render_template('index.html', Display_Box=Display_Box, board_Player=board_Player, msg='red_start')


# reset rote
@app.route('/reset', methods=['post', 'get'])
def reset():
    for i in range(5):
        for j in range(5):
            board_Count[i][j] = 0
            board_Player[i][j] = '0'
            Display_Box[i][j] = '0'
    return render_template('index.html', Display_Box=Display_Box, board_Player=board_Player, msg='red_start')


if __name__ == '__main__':
    app.run(debug=True, port=3456)
