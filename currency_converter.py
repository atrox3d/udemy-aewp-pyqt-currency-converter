from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox
)


from currency_scraper import get_currency


def show_currency():
    input_text = text.text()
    from_currency = from_combo.currentText()
    to_currency = to_combo.currentText()
    rate = get_currency(from_currency, to_currency)
    value = round(float(input_text) * rate, 2)
    print(f'{value=}')
    message = f'{input_text} {from_currency} is {value} {to_currency}'
    output.setText(message)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout.addLayout(layout1)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)
layout3 = QVBoxLayout()
layout1.addLayout(layout3)


currencies = ['USD', 'EUR', 'INR']
from_combo = QComboBox()
from_combo.addItems(currencies)
layout2.addWidget(from_combo)

to_combo = QComboBox()
to_combo.addItems(currencies)
layout2.addWidget(to_combo)

text = QLineEdit()
layout3.addWidget(text)

btn = QPushButton('Convert')
layout3.addWidget(btn)
btn.clicked.connect(show_currency)

output = QLabel('')
layout.addWidget(output)

window.setLayout(layout)
window.show()
app.exec()

