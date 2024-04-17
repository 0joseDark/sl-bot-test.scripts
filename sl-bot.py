import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMenu, QAction, QMessageBox, QGridLayout, QLabel, QPushButton
from secondlife import Client
from pyogre import RenderManager, SceneManager, Camera, Viewport, Node, Entity

class SLBotWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("SL Bot")
        self.resize(1200, 800)

        # Criação do menu
        self.menuBar = QMenu("&Menu")
        self.connectionMenu = QMenu("&Conexão")
        self.actionConnect = QAction("&Conectar", self, triggered=self.connect)
        self.actionDisconnect = QAction("&Desconectar", self, triggered=self.disconnect)
        self.actionExit = QAction("&Sair", self, triggered=self.close)
        self.connectionMenu.addAction(self.actionConnect)
        self.connectionMenu.addAction(self.actionDisconnect)
        self.menuBar.addMenu(self.connectionMenu)
        self.controlMenu = QMenu("&Controle")
        # Adicionar ações de controle do avatar (mover, interagir, etc.)
        self.menuBar.addMenu(self.controlMenu)
        self.commandMenu = QMenu("&Comandos")
        # Adicionar ações para enviar comandos de texto
        self.menuBar.addMenu(self.commandMenu)
        self.setStatusBar(QStatusBar())
        self.setMenuBar(self.menuBar)

        # Criação da área de visualização 3D
        self.viewport = Viewport(None, None)
        self.viewport.setDimensions(800, 600)
        self.scene = SceneManager()
        self.scene.setAmbientLight(Node("AmbientLight", True))
        self.camera = Camera("Camera")
        self.camera.setPosition(0, 0, 10)
        self.camera.lookAt(0, 0, 0)
        self.viewport.scene = self.scene
        self.viewport.camera = self.camera
        self.viewportWidget = QWidget()
        self.viewportWidget.setLayout(QHBoxLayout())
        self.viewportWidget.layout().addWidget(self.viewport)
        self.grid = Grid(self.viewport)

        # Criação dos campos de nome de usuário e senha
        self.nameLabel = QLabel("Nome de Usuário:")
        self.passwordLabel = QLabel("Senha:")
        self.nameLineEdit = QLineEdit()
        self.passwordLineEdit = QLineEdit(echoMode=QLineEdit.Password)

        # Criação do botão de conexão
        self.connectButton = QPushButton("Conectar")
        self.connectButton.clicked.connect(self.connect)

        # Layout da interface
        layout = QGridLayout()
        layout.addWidget(self.viewportWidget, 0, 0, 2, 1)
        layout.addWidget(self.grid, 0, 1)
        layout.addWidget(self.nameLabel, 1, 0)
        layout.addWidget(self.nameLineEdit, 1, 1)
        layout.addWidget(self.passwordLabel, 2, 0)
        layout.addWidget(self.passwordLineEdit, 2, 1)
        layout.addWidget(self.connectButton, 3, 0, 1, 2)

        # Configuração do widget central
