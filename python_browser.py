import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the core web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Create the navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Add a "Back" button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Add a "Forward" button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Add a "Reload" button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Add a "Home" button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Add the URL address bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Keep the URL bar updated if the user clicks a link on a page
        self.browser.urlChanged.connect(self.update_url)

    # Function to handle the Home button
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    # Function to handle when the user hits 'Enter' in the URL bar
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.browser.setUrl(QUrl(url))

    # Function to update the text box when the webpage changes
    def update_url(self, q):
        self.url_bar.setText(q.toString())

# Application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("My Python Browser")
    
    window = SimpleBrowser()
    
    # Start the event loop
    sys.exit(app.exec())