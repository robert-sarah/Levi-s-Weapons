import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QIcon

class LeviWeapons(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Levi's Weapons - Ultimate Kali Tool")
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("gui/assets/logo.png"))
        
        self.tabs = QTabWidget()
        self.tabs.addTab(self.recon_tab(), "Recon")
        self.tabs.addTab(self.wifi_tab(), "Wi-Fi")
        self.tabs.addTab(self.phishing_tab(), "Phishing")
        self.tabs.addTab(self.payload_tab(), "Payloads")
        
        self.setCentralWidget(self.tabs)

    def recon_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Reconnaissance (Whois, Nmap)")
        run_btn = QPushButton("Run Nmap Scan")
        result = QTextEdit()
        result.setReadOnly(True)
        
        run_btn.clicked.connect(lambda: result.setText("Running Nmap..."))
        
        layout.addWidget(label)
        layout.addWidget(run_btn)
        layout.addWidget(result)
        tab.setLayout(layout)
        return tab

    def wifi_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Wi-Fi Attacks"))
        layout.addWidget(QPushButton("Enable Monitor Mode"))
        layout.addWidget(QPushButton("Evil Twin Attack"))
        tab.setLayout(layout)
        return tab

    def phishing_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Phishing Automation"))
        layout.addWidget(QPushButton("Start Fake Login Page"))
        tab.setLayout(layout)
        return tab

    def payload_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Payload Generator"))
        layout.addWidget(QPushButton("Generate Android Payload"))
        layout.addWidget(QPushButton("Generate Windows Payload"))
        tab.setLayout(layout)
        return tab

def start_app():
    app = QApplication(sys.argv)
    window = LeviWeapons()
    window.show()
    sys.exit(app.exec_())
