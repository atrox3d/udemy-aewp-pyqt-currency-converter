from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)


from currency_scraper import get_currency


def show_currency():
    input_text = text.text()
    rate = get_currency('EUR', 'USD')
    value = float(input_text) * rate
    print(value)
    output.setText(str(value))


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currency)

output = QLabel('')
layout.addWidget(output)

window.setLayout(layout)
window.show()
app.exec()

