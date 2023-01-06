from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)


def make_sentence():
    input_text = text.text()
    output.setText(input_text.title() + '.')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentence Maker')

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Make')
layout.addWidget(btn)
btn.clicked.connect(make_sentence)

output = QLabel('')
layout.addWidget(output)

window.setLayout(layout)
window.show()
app.exec()

