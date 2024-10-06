import ctypes
import json
import uuid
import pyqtgraph as pg
import sys

from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from py_toggle import PyToggle
from circular_progress import CircularProgress

FOLDER_DIR = Path("data")
JSON_FILE = FOLDER_DIR / "game_data.json"
SETTINGS_FILE = FOLDER_DIR / "settings.json"

if not FOLDER_DIR.exists():
    FOLDER_DIR.mkdir(parents=True)
    
if not JSON_FILE.exists():
    with open(JSON_FILE, "w") as jsonfile:
        json.dump({"Y1S1":{}}, jsonfile)
        
if not SETTINGS_FILE.exists():
    with open(SETTINGS_FILE, "w") as jsonfile:
        json.dump(
            {
                "Settings":{
                    "Setting_1": False
                }
            }
            , jsonfile)

# Location of your data
BASE_DIR = JSON_FILE

# Ui Elements for Main Window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.actiong = QAction(MainWindow)
        self.actiong.setObjectName(u"actiong")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.settings_button = QPushButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(750, 10, 40, 40))
        self.settings_button.setIconSize(QSize(40, 40))
        self.settings_button.setIcon(QIcon("assets/sliders2.svg"))
        self.settings_button.setStyleSheet("background-color: transparent;" "border: none;")
        self.settings_button.clicked.connect(lambda: {self.settings_window.setVisible(True), self.settings_window.raise_()})
        
        self.settings_window = QWidget(self.centralwidget)
        self.settings_window.setObjectName(u"settings_window")
        self.settings_window.setGeometry(QRect(25, 25, 750, 550))
        self.settings_window.setStyleSheet("background-color: #2d2d2d; border: 2px solid purple; border-radius: 10px;")
        self.settings_window.setVisible(False)
        
        self.settings_window_label = QLabel(self.settings_window)
        self.settings_window_label.setObjectName(u"settings_window_label")
        self.settings_window_label.setGeometry(QRect(20, 10, 730, 30))
        font = QFont()
        font.setFamilies([u"Moon"])
        font.setPointSize(22)
        self.settings_window_label.setFont(font)
        self.settings_window_label.setStyleSheet("Background-color: transparent; border: none; color: White;")
        
        self.settings_window_close_button = QPushButton(self.settings_window)
        self.settings_window_close_button.setObjectName(u"settings_window_close_button")
        self.settings_window_close_button.setGeometry(QRect(710, 10, 30, 30))
        self.settings_window_close_button.setIconSize(QSize(30, 30))
        self.settings_window_close_button.setIcon(QIcon("assets/x-lg.svg"))
        self.settings_window_close_button.setStyleSheet("background-color: transparent;" "border: none;")
        self.settings_window_close_button.clicked.connect(lambda: {self.settings_window.setVisible(False), self.settings_window.raise_()})
        
        self.settings_window_box = QWidget(self.settings_window)
        self.settings_window_box.setObjectName(u"settings_window_box")
        self.settings_window_box.setGeometry(QRect(10, 50, 500, 450))
        self.settings_window_box.setStyleSheet("background-color: transparent; border: none;")
        
        self.settings_window_label_2 = QLabel(self.settings_window)
        self.settings_window_label_2.setObjectName(u"settings_window_label_2")
        self.settings_window_label_2.setGeometry(QRect(10, 50, 300, 30))
        font1 = QFont()
        font1.setFamilies([u"Moon"])
        font1.setPointSize(16)
        self.settings_window_label_2.setFont(font1)
        self.settings_window_label_2.setStyleSheet("Background-color: transparent; border: none; color: White;")
        
        self.toggle_1 = PyToggle()
        self.settings_window_layout = QVBoxLayout(self.settings_window_box)
        self.settings_window_layout.setAlignment(Qt.AlignTop)
        
        # Add a horizontal layout to the vertical layout
        horizontal_layout = QHBoxLayout()
        self.settings_window_layout.addLayout(horizontal_layout)

        # Add the label to the horizontal layout
        horizontal_layout.addWidget(self.settings_window_label_2)

        # Add the toggle to the horizontal layout
        horizontal_layout.addWidget(self.toggle_1)
        
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 50, 801, 551))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 800, 61))
        self.label.setAlignment(Qt.AlignCenter)
        self.credit_label = QLabel(self.tab_1)
        self.credit_label.setObjectName(u"credit_label")
        self.credit_label.setGeometry(QRect(308, 470, 750, 61))
        font = QFont()
        font.setFamilies([u"Moon"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton_new_match = QPushButton(self.tab_1)
        self.pushButton_new_match.setObjectName(u"pushButton_new_match")
        self.pushButton_new_match.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.pushButton_new_match.setGeometry(QRect(270, 220, 251, 61))
        font1 = QFont()
        font1.setFamilies([u"Moon"])
        font1.setPointSize(22)
        self.pushButton_new_match.setFont(font1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 51, 31))
        font2 = QFont()
        font2.setFamilies([u"Moon"])
        font2.setPointSize(12)
        self.credit_label.setFont(font2)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 71, 31))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 71, 31))
        self.label_4.setFont(font2)
        self.spinBox_kills = QSpinBox(self.tab_2)
        self.spinBox_kills.setObjectName(u"spinBox_kills")
        self.spinBox_kills.setGeometry(QRect(110, 90, 131, 31))
        self.spinBox_kills.setFont(font2)
        self.spinBox_deaths = QSpinBox(self.tab_2)
        self.spinBox_deaths.setObjectName(u"spinBox_deaths")
        self.spinBox_deaths.setGeometry(QRect(110, 120, 131, 31))
        self.spinBox_deaths.setFont(font2)
        self.spinBox_assists = QSpinBox(self.tab_2)
        self.spinBox_assists.setObjectName(u"spinBox_assists")
        self.spinBox_assists.setGeometry(QRect(110, 150, 131, 31))
        self.spinBox_assists.setFont(font2)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 60, 71, 31))
        font3 = QFont()
        font3.setFamilies([u"Moon"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.label_5.setFont(font3)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 60, 101, 31))
        self.label_6.setFont(font3)
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 120, 81, 31))
        self.label_7.setFont(font2)
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(260, 150, 81, 31))
        self.label_8.setFont(font2)
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 90, 81, 31))
        self.label_9.setFont(font2)
        self.comboBox_weapon = QComboBox(self.tab_2)
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.setObjectName(u"comboBox_weapon")
        self.comboBox_weapon.setGeometry(QRect(340, 120, 181, 31))
        self.comboBox_weapon.setFont(font2)
        self.comboBox_module = QComboBox(self.tab_2)
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.setObjectName(u"comboBox_module")
        self.comboBox_module.setGeometry(QRect(340, 150, 181, 31))
        self.comboBox_module.setFont(font2)
        self.comboBox_ability = QComboBox(self.tab_2)
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.setObjectName(u"comboBox_ability")
        self.comboBox_ability.setGeometry(QRect(340, 90, 181, 31))
        self.comboBox_ability.setFont(font2)
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(530, 60, 101, 31))
        self.label_10.setFont(font3)
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(530, 120, 81, 31))
        self.label_11.setFont(font2)
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(530, 150, 81, 31))
        self.label_12.setFont(font2)
        self.comboBox_map = QComboBox(self.tab_2)
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.setObjectName(u"comboBox_map")
        self.comboBox_map.setGeometry(QRect(620, 120, 161, 31))
        self.comboBox_map.setFont(font2)
        self.comboBox_win_loss = QComboBox(self.tab_2)
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.setObjectName(u"comboBox_win_loss")
        self.comboBox_win_loss.setGeometry(QRect(620, 150, 161, 31))
        self.comboBox_win_loss.setFont(font2)
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(530, 90, 81, 31))
        self.label_13.setFont(font2)
        self.comboBox_mode = QComboBox(self.tab_2)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName(u"comboBox_mode")
        self.comboBox_mode.setGeometry(QRect(620, 90, 161, 31))
        self.comboBox_mode.setFont(font2)
        self.pushButton_reset = QPushButton(self.tab_2) 
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setGeometry(QRect(480, 460, 101, 41))
        font4 = QFont()
        font4.setFamilies([u"Moon"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.pushButton_reset.setFont(font4)
        self.pushButton_save_game = QPushButton(self.tab_2)
        self.pushButton_save_game.setObjectName(u"pushButton_save_game")
        self.pushButton_save_game.setGeometry(QRect(200, 460, 101, 41))
        self.pushButton_save_game.setFont(font4)
        self.label_71 = QLabel(self.tab_2)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(20, 210, 91, 31))
        self.label_71.setFont(font3)
        self.lineEdit_season = QLineEdit(self.tab_2)
        self.lineEdit_season.setObjectName(u"lineEdit_season")
        self.lineEdit_season.setGeometry(QRect(110, 210, 131, 31))
        self.lineEdit_season.setFont(font2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.scrollArea_2 = QScrollArea(self.tab_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 796, 525))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 777, 624))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.general_statistics = QGroupBox(self.scrollAreaWidgetContents_3)
        self.general_statistics.setObjectName(u"general_statistics")
        self.general_statistics.setMinimumSize(QSize(0, 300))
        self.general_statistics.setMaximumSize(QSize(16777215, 300))
        self.lifetime_kd_lable_general = QLabel(self.general_statistics)
        self.lifetime_kd_lable_general.setObjectName("lifetime_kd_lable_general")
        self.lifetime_kd_lable_general.setGeometry(QRect(10, 20, 200, 31))
        self.lifetime_kd_lable_general.setFont(font3)
        self.lifetime_win_ration_lable_general = QLabel(self.general_statistics)
        self.lifetime_win_ration_lable_general.setObjectName(u"lifetime_win_ration_lable_general")
        self.lifetime_win_ration_lable_general.setGeometry(QRect(240, 20, 230, 31))
        self.lifetime_win_ration_lable_general.setFont(font3)
        self.progressBar_win_ratio_general = QProgressBar(self.general_statistics)
        self.progressBar_win_ratio_general.setObjectName(u"progressBar_win_ratio_general")
        self.progressBar_win_ratio_general.setGeometry(QRect(480, 34, 261, 2))
        self.progressBar_win_ratio_general.setStyleSheet(u"")
        self.progressBar_win_ratio_general.setValue(0)
        self.progressBar_win_ratio_general.setTextVisible(False)
        self.avg_kills_lable_general = QLabel(self.general_statistics)
        self.avg_kills_lable_general.setObjectName(u"avg_kills_lable_general")
        self.avg_kills_lable_general.setGeometry(QRect(10, 50, 200, 31))
        self.avg_kills_lable_general.setFont(font3)
        self.kills_lable_general = QLabel(self.general_statistics)
        self.kills_lable_general.setObjectName(u"kills_lable_general")
        self.kills_lable_general.setGeometry(QRect(10, 80, 200, 31))
        self.kills_lable_general.setFont(font3)
        self.deaths_lable_general = QLabel(self.general_statistics)
        self.deaths_lable_general.setObjectName(u"deaths_lable_general")
        self.deaths_lable_general.setGeometry(QRect(10, 110, 200, 31))
        self.deaths_lable_general.setFont(font3)
        self.assists_lable_general = QLabel(self.general_statistics)
        self.assists_lable_general.setObjectName(u"assists_lable_general")
        self.assists_lable_general.setGeometry(QRect(10, 140, 200, 31))
        self.assists_lable_general.setFont(font3)
        self.wins_lable_general = QLabel(self.general_statistics)
        self.wins_lable_general.setObjectName(u"wins_lable_general")
        self.wins_lable_general.setGeometry(QRect(240, 50, 200, 31))
        self.wins_lable_general.setFont(font3)
        self.losses_lable_general = QLabel(self.general_statistics)
        self.losses_lable_general.setObjectName(u"losses_lable_general")
        self.losses_lable_general.setGeometry(QRect(240, 80, 200, 31))
        self.losses_lable_general.setFont(font3)
        self.matches_lable_general = QLabel(self.general_statistics)
        self.matches_lable_general.setObjectName(u"matches_lable_general")
        self.matches_lable_general.setGeometry(QRect(240, 110, 200, 31))
        self.matches_lable_general.setFont(font3)
        self.most_used_ability_lable_general = QLabel(self.general_statistics)
        self.most_used_ability_lable_general.setObjectName(u"most_used_ability_lable_general")
        self.most_used_ability_lable_general.setGeometry(QRect(10, 200, 420, 31))
        self.most_used_ability_lable_general.setFont(font3)
        self.most_used_weapon_lable_general = QLabel(self.general_statistics)
        self.most_used_weapon_lable_general.setObjectName(u"most_used_weapon_lable_general")
        self.most_used_weapon_lable_general.setGeometry(QRect(10, 230, 420, 31))
        self.most_used_weapon_lable_general.setFont(font3)
        self.most_used_module_lable_general = QLabel(self.general_statistics)
        self.most_used_module_lable_general.setObjectName(u"most_used_module_lable_general")
        self.most_used_module_lable_general.setGeometry(QRect(10, 260, 420, 31))
        self.most_used_module_lable_general.setFont(font3)
        self.best_map_lable_general = QLabel(self.general_statistics)
        self.best_map_lable_general.setObjectName(u"best_map_lable_general")
        self.best_map_lable_general.setGeometry(QRect(440, 260, 300, 31))
        self.best_map_lable_general.setFont(font3)
        self.best_weapon_lable_general = QLabel(self.general_statistics)
        self.best_weapon_lable_general.setObjectName(u"best_weapon_lable_general")
        self.best_weapon_lable_general.setGeometry(QRect(440, 230, 300, 31))
        self.best_weapon_lable_general.setFont(font3)
        self.best_mode_lable_general = QLabel(self.general_statistics)
        self.best_mode_lable_general.setObjectName(u"best_mode_lable_general")
        self.best_mode_lable_general.setGeometry(QRect(440, 200, 300, 31))
        self.best_mode_lable_general.setFont(font3)

        self.verticalLayout_2.addWidget(self.general_statistics)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.scrollArea = QScrollArea(self.tab_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 796, 525))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 779, 509))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_4, "")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 10, 800, 31))
        font6 = QFont()
        font6.setFamilies([u"Moon"])
        font6.setPointSize(24)
        self.label_14.setFont(font6)
        font7 = QFont()
        font7.setFamilies([u"Moon"])
        font7.setPointSize(10)
        self.tabWidget.setFont(font7)
        
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        
        # Scroll area for the graph
        self.scrollArea_3 = QScrollArea(self.tab_5)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 796, 525))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Frame for the scroll area
        self.filler = QFrame()
        self.filler.setObjectName(u"filler")
        self.filler.setGeometry(QRect(0, 0, 775, 525))
        self.scrollArea_3.setWidget(self.filler)
        
        # Selection box for the modes
        self.selection_box = QFrame(self.filler)
        self.selection_box.setObjectName(u"selection_box")
        self.selection_box.setGeometry(QRect(5, 470, 775, 60))
        self.selection_box.setFont(font2)
        
        # Button for all modes
        self.button1 = QPushButton(self.selection_box)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(0, 10, 100, 40))
        self.button1.setFont(font2)
        self.button1.setStyleSheet(u"color: purple;")
        
        # Button for Backup
        self.button2 = QPushButton(self.selection_box)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(105, 10, 100, 40))
        self.button2.setFont(font2)
        
        # Button for Q-Ball
        self.button3 = QPushButton(self.selection_box)
        self.button3.setObjectName(u"button3")
        self.button3.setGeometry(QRect(210, 10, 100, 40))
        self.button3.setFont(font2)
        
        # Button for Free For All
        self.button4 = QPushButton(self.selection_box)
        self.button4.setObjectName(u"button4")
        self.button4.setGeometry(QRect(315, 10, 100, 40))
        self.button4.setFont(font2)
        
        # Button for Ranked
        self.button5 = QPushButton(self.selection_box)
        self.button5.setObjectName(u"button5")
        self.button5.setGeometry(QRect(420, 10, 100, 40))
        self.button5.setFont(font2)
        
        # Combo box for the stats
        self.statistic_box = QComboBox(self.selection_box)
        self.statistic_box.setObjectName(u"statistic_box")
        self.statistic_box.setGeometry(QRect(525, 10, 115, 40))
        self.statistic_box.setFont(font2)
        self.statistic_box.addItem("")  #K/D
        self.statistic_box.addItem("")  #Kills
        self.statistic_box.addItem("")  #Deaths
        self.statistic_box.addItem("")  #Matches
        self.statistic_box.addItem("")  #Wins
        self.statistic_box.addItem("")  #Losses
        self.statistic_box.addItem("")  #Win%
        
        # Combo box for the time frame
        self.time_box = QComboBox(self.selection_box)
        self.time_box.setObjectName(u"time_box")
        self.time_box.setGeometry(QRect(645, 10, 130, 40))
        self.time_box.setFont(font2)
        self.time_box.addItem("")  # All time
        self.time_box.addItem("")  # Last Month
        self.time_box.addItem("")  # Last Week
        
        # The graph
        self.graph = pg.PlotWidget(self.filler)
        self.graph.setObjectName(u"graph")
        self.graph.setGeometry(QRect(5, 5, 775, 460))
        self.graph.setMouseEnabled(x=False, y=False)
        self.graph.setBackground('#2D2D2D')
        self.graph.showGrid(x=True, y=True)
        
        # Design 1
        self.design_1 = QFrame(self.filler)
        self.design_1.setObjectName(u"design_1")
        self.design_1.setGeometry(QRect(5, 550, 775, 600))
        self.design_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.design_1.setFrameShadow(QFrame.Shadow.Raised)
        self.design_1.hide()
        
        # Design 2
        self.design_2 = QFrame(self.filler)
        self.design_2.setObjectName(u"design_2")
        self.design_2.setGeometry(QRect(5, 550, 775, 515))
        self.design_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.design_2.setFrameShadow(QFrame.Shadow.Raised)
        
        # Design 2 - ComboBoxes for Weapons
        self.design_2_ComboBox_Weapon = QComboBox(self.design_2)
        self.design_2_ComboBox_Weapon.setObjectName(u"design_2_ComboBox_Weapon")
        self.design_2_ComboBox_Weapon.setGeometry(QRect(30, 10, 170, 40))
        self.design_2_ComboBox_Weapon.setFont(font7)
        self.design_2_ComboBox_Weapon.addItem("")
        self.design_2_ComboBox_Weapon.addItem("")
        self.design_2_ComboBox_Weapon.addItem("")
        self.design_2_ComboBox_Weapon.addItem("")
        self.design_2_ComboBox_Weapon.addItem("")
        self.design_2_ComboBox_Weapon.addItem("")
        self.design_2_ComboBox_Weapon.addItem("")
        
        # Design 2 - ComboBoxes for Modules
        self.design_2_ComboBox_Module = QComboBox(self.design_2)
        self.design_2_ComboBox_Module.setObjectName(u"design_2_ComboBox_Module")
        self.design_2_ComboBox_Module.setGeometry(QRect(210, 10, 170, 40))
        self.design_2_ComboBox_Module.setFont(font7)
        self.design_2_ComboBox_Module.addItem("")
        self.design_2_ComboBox_Module.addItem("")
        self.design_2_ComboBox_Module.addItem("")
        self.design_2_ComboBox_Module.addItem("")
        self.design_2_ComboBox_Module.addItem("")
        self.design_2_ComboBox_Module.addItem("")
        self.design_2_ComboBox_Module.addItem("")
        
        # Design 2 - ComboBoxes for Abilities
        self.design_2_ComboBox_Ability = QComboBox(self.design_2)
        self.design_2_ComboBox_Ability.setObjectName(u"design_2_ComboBox_Ability")
        self.design_2_ComboBox_Ability.setGeometry(QRect(390, 10, 170, 40))
        self.design_2_ComboBox_Ability.setFont(font7)
        self.design_2_ComboBox_Ability.addItem("")
        self.design_2_ComboBox_Ability.addItem("")
        self.design_2_ComboBox_Ability.addItem("")
        self.design_2_ComboBox_Ability.addItem("")
        self.design_2_ComboBox_Ability.addItem("")
        self.design_2_ComboBox_Ability.addItem("")
        self.design_2_ComboBox_Ability.addItem("")
        
        # Design 2 - ComboBoxes for Maps
        self.design_2_ComboBox_Map = QComboBox(self.design_2)
        self.design_2_ComboBox_Map.setObjectName(u"design_2_ComboBox_Map")
        self.design_2_ComboBox_Map.setGeometry(QRect(570, 10, 170, 40))
        self.design_2_ComboBox_Map.setFont(font7)
        self.design_2_ComboBox_Map.addItem("")
        self.design_2_ComboBox_Map.addItem("")
        self.design_2_ComboBox_Map.addItem("")
        self.design_2_ComboBox_Map.addItem("")
        self.design_2_ComboBox_Map.addItem("")
        self.design_2_ComboBox_Map.addItem("")
        
        # Dummy Image
        self.dummy_image = QLabel(self.design_2)
        self.dummy_image.setObjectName(u"dummy_image")
        self.dummy_image.setGeometry(QRect(30, 220, 710, 290))
        self.dummy_image.setPixmap(QPixmap(u"assets/Blette.png"))
        self.dummy_image.setScaledContents(True)
        
        # Design 2 - Tabs
        self.design_2_tab = QTabWidget(self.design_2)
        self.design_2_tab.setObjectName(u"design_2_tab")
        self.design_2_tab.setGeometry(QRect(30, 60, 710, 150))
        self.design_2_tab.setFont(font7)
        self.design_2_tab.addTab(QWidget(), "Weapons")
        self.design_2_tab.addTab(QWidget(), "Modules")
        self.design_2_tab.addTab(QWidget(), "Abilities")
        self.design_2_tab.addTab(QWidget(), "Maps")
        
        # Design 2 - Tab 1 - Weapon
        self.design_2_tab_1_text = QLabel(self.design_2_tab.widget(0))
        self.design_2_tab_1_text.setObjectName(u"design_2_tab_1_text")
        self.design_2_tab_1_text.setGeometry(QRect(10, 10, 400, 30))
        self.design_2_tab_1_text.setFont(font6)
        
        # Design 2 - Tab 1 - K/D
        self.design_2_tab_1_kd = QLabel(self.design_2_tab.widget(0))
        self.design_2_tab_1_kd.setObjectName(u"design_2_tab_1_kd")
        self.design_2_tab_1_kd.setGeometry(QRect(10, 50, 300, 30))
        self.design_2_tab_1_kd.setFont(font3)
        
        # Design 2 - Tab 1 - K/D Progress
        self.design_2_tab_1_kd_progress = QProgressBar(self.design_2_tab.widget(0))
        self.design_2_tab_1_kd_progress.setObjectName(u"design_2_tab_1_kd_progress")
        self.design_2_tab_1_kd_progress.setGeometry(QRect(350, 55, 265, 20))
        self.design_2_tab_1_kd_progress.setFont(font3)
        self.design_2_tab_1_kd_progress.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: darkgray;} QProgressBar::chunk { background-color: purple; border-radius: 10px; }")
        self.design_2_tab_1_kd_progress.setFormat("K/D: 0/0")
        
        # Design 2 - Tab 1 - Kills
        self.design_2_tab_1_kills_label = QLabel("Kills", self.design_2_tab.widget(0))
        self.design_2_tab_1_kills_label.setObjectName(u"design_2_tab_1_kills_label")
        self.design_2_tab_1_kills_label.setGeometry(QRect(280, 50, 300, 30))
        self.design_2_tab_1_kills_label.setFont(font2)
        
        # Design 2 - Tab 1 - Deaths
        self.design_2_tab_1_deaths_label = QLabel("Deaths", self.design_2_tab.widget(0))
        self.design_2_tab_1_deaths_label.setObjectName(u"design_2_tab_1_deaths_label")
        self.design_2_tab_1_deaths_label.setGeometry(QRect(630, 50, 300, 30))
        self.design_2_tab_1_deaths_label.setFont(font2)
        
        # Design 2 - Tab 1 - Usage
        self.design_2_tab_1_usage = QLabel(self.design_2_tab.widget(0))
        self.design_2_tab_1_usage.setObjectName(u"design_2_tab_1_usage")
        self.design_2_tab_1_usage.setGeometry(QRect(10, 90, 300, 30))
        self.design_2_tab_1_usage.setFont(font3)
        
        # Design 2 - Tab 1 - Winrate Progress
        self.design_2_tab_1_usage_progress = QProgressBar(self.design_2_tab.widget(0))
        self.design_2_tab_1_usage_progress.setObjectName(u"design_2_tab_1_usage_progress")
        self.design_2_tab_1_usage_progress.setGeometry(QRect(350, 95, 265, 20))
        self.design_2_tab_1_usage_progress.setFont(font3)
        self.design_2_tab_1_usage_progress.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: darkgray;} QProgressBar::chunk { background-color: purple; border-radius: 10px;}")
        self.design_2_tab_1_usage_progress.setFormat("Winrate: 0%")
        
        # Design 2 - Tab 1 - Wins
        self.design_2_tab_1_wins_label = QLabel("Wins", self.design_2_tab.widget(0))
        self.design_2_tab_1_wins_label.setObjectName(u"design_2_tab_1_wins_label")
        self.design_2_tab_1_wins_label.setGeometry(QRect(280, 90, 300, 30))
        self.design_2_tab_1_wins_label.setFont(font2)
        
        # Design 2 - Tab 1 - Losses
        self.design_2_tab_1_losses_label = QLabel("Losses", self.design_2_tab.widget(0))
        self.design_2_tab_1_losses_label.setObjectName(u"design_2_tab_1_losses_label")
        self.design_2_tab_1_losses_label.setGeometry(QRect(630, 90, 300, 30))
        self.design_2_tab_1_losses_label.setFont(font2)
        
        # Design 2 - Tab 2 - Module
        self.design_2_tab_2_text = QLabel(self.design_2_tab.widget(1))
        self.design_2_tab_2_text.setObjectName(u"design_2_tab_2_text")
        self.design_2_tab_2_text.setGeometry(QRect(10, 10, 400, 30))
        self.design_2_tab_2_text.setFont(font6)
        
        # Design 2 - Tab 2 - Usage
        self.design_2_tab_2_usage = QLabel(self.design_2_tab.widget(1))
        self.design_2_tab_2_usage.setObjectName(u"design_2_tab_2_usage")
        self.design_2_tab_2_usage.setGeometry(QRect(10, 90, 300, 30))
        self.design_2_tab_2_usage.setFont(font3)
        
        # Design 2 - Tab 2 - Usage Progress
        self.design_2_tab_2_usage_progress = QProgressBar(self.design_2_tab.widget(1))
        self.design_2_tab_2_usage_progress.setObjectName(u"design_2_tab_2_usage_progress")
        self.design_2_tab_2_usage_progress.setGeometry(QRect(350, 95, 265, 20))
        self.design_2_tab_2_usage_progress.setFont(font3)
        self.design_2_tab_2_usage_progress.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: darkgray;} QProgressBar::chunk { background-color: purple; border-radius: 10px;}")
        self.design_2_tab_2_usage_progress.setFormat("Winrate: 0%")
        
        # Design 2 - Tab 2 - Wins
        self.design_2_tab_2_wins_label = QLabel("Wins", self.design_2_tab.widget(1))
        self.design_2_tab_2_wins_label.setObjectName(u"design_2_tab_2_wins_label")
        self.design_2_tab_2_wins_label.setGeometry(QRect(280, 90, 300, 30))
        self.design_2_tab_2_wins_label.setFont(font2)
        
        # Design 2 - Tab 2 - Losses
        self.design_2_tab_2_losses_label = QLabel("Losses", self.design_2_tab.widget(1))
        self.design_2_tab_2_losses_label.setObjectName(u"design_2_tab_2_losses_label")
        self.design_2_tab_2_losses_label.setGeometry(QRect(630, 90, 300, 30))
        self.design_2_tab_2_losses_label.setFont(font2)
        
        # Design 2 - Tab 3 - Module
        self.design_2_tab_3_text = QLabel(self.design_2_tab.widget(2))
        self.design_2_tab_3_text.setObjectName(u"design_2_tab_3_text")
        self.design_2_tab_3_text.setGeometry(QRect(10, 10, 400, 30))
        self.design_2_tab_3_text.setFont(font6)
        
        # Design 2 - Tab 3 - Usage
        self.design_2_tab_3_usage = QLabel(self.design_2_tab.widget(2))
        self.design_2_tab_3_usage.setObjectName(u"design_2_tab_3_usage")
        self.design_2_tab_3_usage.setGeometry(QRect(10, 90, 300, 30))
        self.design_2_tab_3_usage.setFont(font3)
        
        # Design 2 - Tab 3 - Usage Progress
        self.design_2_tab_3_usage_progress = QProgressBar(self.design_2_tab.widget(2))
        self.design_2_tab_3_usage_progress.setObjectName(u"design_2_tab_3_usage_progress")
        self.design_2_tab_3_usage_progress.setGeometry(QRect(350, 95, 265, 20))
        self.design_2_tab_3_usage_progress.setFont(font3)
        self.design_2_tab_3_usage_progress.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: darkgray;} QProgressBar::chunk { background-color: purple; border-radius: 10px;}")
        self.design_2_tab_3_usage_progress.setFormat("Winrate: 0%")
        
        # Design 2 - Tab 3 - Wins
        self.design_2_tab_3_wins_label = QLabel("Wins", self.design_2_tab.widget(2))
        self.design_2_tab_3_wins_label.setObjectName(u"design_2_tab_3_wins_label")
        self.design_2_tab_3_wins_label.setGeometry(QRect(280, 90, 300, 30))
        self.design_2_tab_3_wins_label.setFont(font2)
        
        # Design 2 - Tab 3 - Losses
        self.design_2_tab_3_losses_label = QLabel("Losses", self.design_2_tab.widget(2))
        self.design_2_tab_3_losses_label.setObjectName(u"design_2_tab_3_losses_label")
        self.design_2_tab_3_losses_label.setGeometry(QRect(630, 90, 300, 30))
        self.design_2_tab_3_losses_label.setFont(font2)
        
        # Design 2 - Tab 4 - Map
        self.design_2_tab_4_text = QLabel(self.design_2_tab.widget(3))
        self.design_2_tab_4_text.setObjectName(u"design_2_tab_4_text")
        self.design_2_tab_4_text.setGeometry(QRect(10, 10, 400, 30))
        self.design_2_tab_4_text.setFont(font6)
        
        # Design 2 - Tab 4 - K/D
        self.design_2_tab_4_kd = QLabel(self.design_2_tab.widget(3))
        self.design_2_tab_4_kd.setObjectName(u"design_2_tab_4_kd")
        self.design_2_tab_4_kd.setGeometry(QRect(10, 50, 300, 30))
        self.design_2_tab_4_kd.setFont(font3)
        
        # Design 2 - Tab 4 - K/D Progress
        self.design_2_tab_4_kd_progress = QProgressBar(self.design_2_tab.widget(3))
        self.design_2_tab_4_kd_progress.setObjectName(u"design_2_tab_4_kd_progress")
        self.design_2_tab_4_kd_progress.setGeometry(QRect(350, 55, 265, 20))
        self.design_2_tab_4_kd_progress.setFont(font3)
        self.design_2_tab_4_kd_progress.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: darkgray;} QProgressBar::chunk { background-color: purple; border-radius: 10px;}")
        self.design_2_tab_4_kd_progress.setFormat("Winrate: 0%")
        
        # Design 2 - Tab 4 - Kills
        self.design_2_tab_4_kills_label = QLabel("Kills", self.design_2_tab.widget(3))
        self.design_2_tab_4_kills_label.setObjectName(u"design_2_tab_4_kills_label")
        self.design_2_tab_4_kills_label.setGeometry(QRect(280, 50, 300, 30))
        self.design_2_tab_4_kills_label.setFont(font2)
        
        # Design 2 - Tab 4 - Deaths
        self.design_2_tab_4_deaths_label = QLabel("Deaths", self.design_2_tab.widget(3))
        self.design_2_tab_4_deaths_label.setObjectName(u"design_2_tab_4_deaths_label")
        self.design_2_tab_4_deaths_label.setGeometry(QRect(630, 50, 300, 30))
        self.design_2_tab_4_deaths_label.setFont(font2)
        
        # Design 2 - Tab 4 - Usage
        self.design_2_tab_4_usage = QLabel(self.design_2_tab.widget(3))
        self.design_2_tab_4_usage.setObjectName(u"design_2_tab_4_usage")
        self.design_2_tab_4_usage.setGeometry(QRect(10, 90, 300, 30))
        self.design_2_tab_4_usage.setFont(font3)
        
        # Design 2 - Tab 4 - Usage Progress
        self.design_2_tab_4_usage_progress = QProgressBar(self.design_2_tab.widget(3))
        self.design_2_tab_4_usage_progress.setObjectName(u"design_2_tab_4_usage_progress")
        self.design_2_tab_4_usage_progress.setGeometry(QRect(350, 95, 265, 20))
        self.design_2_tab_4_usage_progress.setFont(font3)
        self.design_2_tab_4_usage_progress.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: darkgray;} QProgressBar::chunk { background-color: purple; border-radius: 10px;}")
        self.design_2_tab_4_usage_progress.setFormat("Winrate: 0%")
        
        # Design 2 - Tab 4 - Wins
        self.design_2_tab_4_wins_label = QLabel("Wins", self.design_2_tab.widget(3))
        self.design_2_tab_4_wins_label.setObjectName(u"design_2_tab_4_wins_label")
        self.design_2_tab_4_wins_label.setGeometry(QRect(280, 90, 300, 30))
        self.design_2_tab_4_wins_label.setFont(font2)
        
        # Design 2 - Tab 4 - Losses
        self.design_2_tab_4_losses_label = QLabel("Losses", self.design_2_tab.widget(3))
        self.design_2_tab_4_losses_label.setObjectName(u"design_2_tab_4_losses_label")
        self.design_2_tab_4_losses_label.setGeometry(QRect(630, 90, 300, 30))
        self.design_2_tab_4_losses_label.setFont(font2)
        
        self.design_2.hide()
        
        self.tabWidget.addTab(self.tab_5, "")
        self.settings_button.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BattleCore Tracker", None))
        self.actiong.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BattleCore Tracker - V.2.2", None))
        self.credit_label.setText(QCoreApplication.translate("MainWindow", u"Created by: Puppetino", None))
        self.pushButton_new_match.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Kills:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Assists:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"K/D/A", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Loadout", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Weapon:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Module:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ability:", None))
        self.comboBox_weapon.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.comboBox_weapon.setItemText(1, QCoreApplication.translate("MainWindow", u" Sparks", None))
        self.comboBox_weapon.setItemText(2, QCoreApplication.translate("MainWindow", u" Storm", None))
        self.comboBox_weapon.setItemText(3, QCoreApplication.translate("MainWindow", u" Orion", None))
        self.comboBox_weapon.setItemText(4, QCoreApplication.translate("MainWindow", u" Pulser", None))
        self.comboBox_weapon.setItemText(5, QCoreApplication.translate("MainWindow", u" Vortex-5", None))
        self.comboBox_weapon.setItemText(6, QCoreApplication.translate("MainWindow", u" Nova", None))

        self.comboBox_module.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.comboBox_module.setItemText(1, QCoreApplication.translate("MainWindow", u" Regeneration", None))
        self.comboBox_module.setItemText(2, QCoreApplication.translate("MainWindow", u" Mobility", None))
        self.comboBox_module.setItemText(3, QCoreApplication.translate("MainWindow", u" Vampirism", None))
        self.comboBox_module.setItemText(4, QCoreApplication.translate("MainWindow", u" Berserker", None))
        self.comboBox_module.setItemText(5, QCoreApplication.translate("MainWindow", u" Heal Booster", None))
        self.comboBox_module.setItemText(6, QCoreApplication.translate("MainWindow", u" Synchronisation", None))

        self.comboBox_ability.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.comboBox_ability.setItemText(1, QCoreApplication.translate("MainWindow", u" Blast", None))
        self.comboBox_ability.setItemText(2, QCoreApplication.translate("MainWindow", u" Shield Healing", None))
        self.comboBox_ability.setItemText(3, QCoreApplication.translate("MainWindow", u" Teleportation", None))
        self.comboBox_ability.setItemText(4, QCoreApplication.translate("MainWindow", u" Invisibility", None))
        self.comboBox_ability.setItemText(5, QCoreApplication.translate("MainWindow", u" Flash Bang", None))
        self.comboBox_ability.setItemText(6, QCoreApplication.translate("MainWindow", u" Black Hole", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Map:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Win/Loss:", None))
        self.comboBox_map.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.comboBox_map.setItemText(1, QCoreApplication.translate("MainWindow", u" Trinity Island", None))
        self.comboBox_map.setItemText(2, QCoreApplication.translate("MainWindow", u" Shroomworld", None))
        self.comboBox_map.setItemText(3, QCoreApplication.translate("MainWindow", u" Lost Complex", None))
        self.comboBox_map.setItemText(4, QCoreApplication.translate("MainWindow", u" Twilight Path", None))
        self.comboBox_map.setItemText(5, QCoreApplication.translate("MainWindow", u" Singularity", None))

        self.comboBox_win_loss.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.comboBox_win_loss.setItemText(1, QCoreApplication.translate("MainWindow", u" Win", None))
        self.comboBox_win_loss.setItemText(2, QCoreApplication.translate("MainWindow", u" loss", None))
        self.comboBox_win_loss.setItemText(3, QCoreApplication.translate("MainWindow", u" Draw", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.comboBox_mode.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("MainWindow", u" Backup", None))
        self.comboBox_mode.setItemText(2, QCoreApplication.translate("MainWindow", u" Q-Ball", None))
        self.comboBox_mode.setItemText(3, QCoreApplication.translate("MainWindow", u" Free for All", None))
        self.comboBox_mode.setItemText(4, QCoreApplication.translate("MainWindow", u" Ranked", None))
        self.comboBox_mode.setItemText(5, QCoreApplication.translate("MainWindow", u" Co-op vs. AIs", None))
        self.comboBox_mode.setItemText(6, QCoreApplication.translate("MainWindow", u" Custom", None))

        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_save_game.setText(QCoreApplication.translate("MainWindow", u"Save Game", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Season:", None))
        self.lineEdit_season.setText(QCoreApplication.translate("MainWindow", u"Y1S1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"New Game", None))
        self.general_statistics.setTitle(QCoreApplication.translate("MainWindow", u"General Statistics", None))
        self.lifetime_kd_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lifetime_win_ration_lable_general.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.avg_kills_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.kills_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.deaths_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.assists_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.wins_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.losses_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.matches_lable_general.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.most_used_ability_lable_general.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.most_used_weapon_lable_general.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.most_used_module_lable_general.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.best_map_lable_general.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.best_weapon_lable_general.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.best_mode_lable_general.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"History", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"BattleCore Tracker", None))
        
        self.button1.setText(QCoreApplication.translate("MainWindow", u"All Modes", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"Q-Ball", None))
        self.button4.setText(QCoreApplication.translate("MainWindow", u"FFA", None))
        self.button5.setText(QCoreApplication.translate("MainWindow", u"Ranked", None))
        
        self.statistic_box.setItemText(0, QCoreApplication.translate("MainWindow", u" K/D", None))
        self.statistic_box.setItemText(1, QCoreApplication.translate("MainWindow", u" Kills", None))
        self.statistic_box.setItemText(2, QCoreApplication.translate("MainWindow", u" Deaths", None))
        self.statistic_box.setItemText(3, QCoreApplication.translate("MainWindow", u" Matches", None))
        self.statistic_box.setItemText(4, QCoreApplication.translate("MainWindow", u" Wins", None))
        self.statistic_box.setItemText(5, QCoreApplication.translate("MainWindow", u" Losses", None))
        self.statistic_box.setItemText(6, QCoreApplication.translate("MainWindow", u" Win%", None))
        
        self.time_box.setItemText(0, QCoreApplication.translate("MainWindow", u" Last Year", None))
        self.time_box.setItemText(1, QCoreApplication.translate("MainWindow", u" Last Month", None))
        self.time_box.setItemText(2, QCoreApplication.translate("MainWindow", u" Last Week", None))
        
        # self.dummy_text.setText(QCoreApplication.translate("MainWindow", u"SOON\u2122", None))
        
        self.settings_window_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.settings_window_label_2.setText(QCoreApplication.translate("MainWindow", u"Design 2 for the Analytics Tab", None))
        
        self.design_2_ComboBox_Weapon.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.design_2_ComboBox_Weapon.setItemText(1, QCoreApplication.translate("MainWindow", u" Sparks", None))
        self.design_2_ComboBox_Weapon.setItemText(2, QCoreApplication.translate("MainWindow", u" Storm", None))
        self.design_2_ComboBox_Weapon.setItemText(3, QCoreApplication.translate("MainWindow", u" Orion", None))
        self.design_2_ComboBox_Weapon.setItemText(4, QCoreApplication.translate("MainWindow", u" Pulser", None))
        self.design_2_ComboBox_Weapon.setItemText(5, QCoreApplication.translate("MainWindow", u" Vortex-5", None))
        self.design_2_ComboBox_Weapon.setItemText(6, QCoreApplication.translate("MainWindow", u" Nova", None))
        
        self.design_2_ComboBox_Ability.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.design_2_ComboBox_Ability.setItemText(1, QCoreApplication.translate("MainWindow", u" Blast", None))
        self.design_2_ComboBox_Ability.setItemText(2, QCoreApplication.translate("MainWindow", u" Shield Healing", None))
        self.design_2_ComboBox_Ability.setItemText(3, QCoreApplication.translate("MainWindow", u" Teleportation", None))
        self.design_2_ComboBox_Ability.setItemText(4, QCoreApplication.translate("MainWindow", u" Invisibility", None))
        self.design_2_ComboBox_Ability.setItemText(5, QCoreApplication.translate("MainWindow", u" Flash Bang", None))
        self.design_2_ComboBox_Ability.setItemText(6, QCoreApplication.translate("MainWindow", u" Black Hole", None))
        
        self.design_2_ComboBox_Module.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.design_2_ComboBox_Module.setItemText(1, QCoreApplication.translate("MainWindow", u" Regeneration", None))
        self.design_2_ComboBox_Module.setItemText(2, QCoreApplication.translate("MainWindow", u" Mobility", None))
        self.design_2_ComboBox_Module.setItemText(3, QCoreApplication.translate("MainWindow", u" Vampirism", None))
        self.design_2_ComboBox_Module.setItemText(4, QCoreApplication.translate("MainWindow", u" Berserker", None))
        self.design_2_ComboBox_Module.setItemText(5, QCoreApplication.translate("MainWindow", u" Heal Booster", None))
        self.design_2_ComboBox_Module.setItemText(6, QCoreApplication.translate("MainWindow", u" Synchronisation", None))
        
        self.design_2_ComboBox_Map.setItemText(0, QCoreApplication.translate("MainWindow", u" None", None))
        self.design_2_ComboBox_Map.setItemText(1, QCoreApplication.translate("MainWindow", u" Trinity Island", None))
        self.design_2_ComboBox_Map.setItemText(2, QCoreApplication.translate("MainWindow", u" Shroomworld", None))
        self.design_2_ComboBox_Map.setItemText(3, QCoreApplication.translate("MainWindow", u" Lost Complex", None))
        self.design_2_ComboBox_Map.setItemText(4, QCoreApplication.translate("MainWindow", u" Twilight Path", None))
        self.design_2_ComboBox_Map.setItemText(5, QCoreApplication.translate("MainWindow", u" Singularity", None))
        
        self.design_2_tab_1_text.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.design_2_tab_1_kd.setText(QCoreApplication.translate("MainWindow", u"K/D: NONE", None))
        self.design_2_tab_1_usage.setText(QCoreApplication.translate("MainWindow", u"Usage: NONE", None))
        
        self.design_2_tab_2_text.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.design_2_tab_2_usage.setText(QCoreApplication.translate("MainWindow", u"Usage: NONE", None))
        
        self.design_2_tab_3_text.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.design_2_tab_3_usage.setText(QCoreApplication.translate("MainWindow", u"Usage: NONE", None))
        
        self.design_2_tab_4_text.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.design_2_tab_4_kd.setText(QCoreApplication.translate("MainWindow", u"K/D: NONE", None))
        self.design_2_tab_4_usage.setText(QCoreApplication.translate("MainWindow", u"Usage: NONE", None))
        
        

    # retranslateUi

# Ui Elements for the Game Data Editor
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 110)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_game_1 = QFrame(self.centralwidget)
        self.frame_game_1.setObjectName(u"frame_game_1")
        self.frame_game_1.setGeometry(QRect(0, 0, 761, 110))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_game_1.sizePolicy().hasHeightForWidth())
        self.frame_game_1.setSizePolicy(sizePolicy)
        self.frame_game_1.setMinimumSize(QSize(761, 110))
        self.frame_game_1.setMaximumSize(QSize(761, 110))
        self.frame_game_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_game_1.setFrameShadow(QFrame.Shadow.Raised)
        self.label_41 = QLabel(self.frame_game_1)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 10, 61, 21))
        font = QFont()
        font.setFamilies([u"Moon"])
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_42 = QLabel(self.frame_game_1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(200, 10, 100, 21))
        self.label_42.setFont(font)
        self.label_43 = QLabel(self.frame_game_1)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 40, 71, 16))
        self.label_43.setFont(font)
        self.label_44 = QLabel(self.frame_game_1)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 60, 71, 16))
        self.label_44.setFont(font)
        self.label_45 = QLabel(self.frame_game_1)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 80, 71, 16))
        self.label_45.setFont(font)
        self.label_46 = QLabel(self.frame_game_1)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(170, 60, 81, 16))
        self.label_46.setFont(font)
        self.label_47 = QLabel(self.frame_game_1)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(170, 40, 81, 16))
        self.label_47.setFont(font)
        self.label_48 = QLabel(self.frame_game_1)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(170, 80, 81, 16))
        self.label_48.setFont(font)
        self.label_49 = QLabel(self.frame_game_1)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(340, 10, 91, 21))
        self.label_49.setFont(font)
        self.label_50 = QLabel(self.frame_game_1)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(410, 60, 61, 16))
        self.label_50.setFont(font)
        self.label_51 = QLabel(self.frame_game_1)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(410, 40, 61, 16))
        self.label_51.setFont(font)
        self.label_52 = QLabel(self.frame_game_1)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(410, 80, 61, 16))
        self.label_52.setFont(font)
        self.pushButton_delete = QPushButton(self.frame_game_1)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(640, 70, 75, 24))
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.label_64 = QLabel(self.frame_game_1)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(580, 10, 71, 21))
        self.label_64.setFont(font)
        self.spinBox_kills = QSpinBox(self.frame_game_1)
        self.spinBox_kills.setObjectName(u"spinBox_kills")
        self.spinBox_kills.setGeometry(QRect(80, 36, 30, 21))
        font1 = QFont()
        font1.setFamilies([u"Moon"])
        font1.setPointSize(10)
        self.spinBox_kills.setFont(font1)
        self.spinBox_deaths = QSpinBox(self.frame_game_1)
        self.spinBox_deaths.setObjectName(u"spinBox_deaths")
        self.spinBox_deaths.setGeometry(QRect(80, 56, 30, 21))
        self.spinBox_deaths.setFont(font1)
        self.spinBox_assists = QSpinBox(self.frame_game_1)
        self.spinBox_assists.setObjectName(u"spinBox_assists")
        self.spinBox_assists.setGeometry(QRect(80, 76, 30, 21))
        self.spinBox_assists.setFont(font1)
        self.comboBox_ability = QComboBox(self.frame_game_1)
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.addItem("")
        self.comboBox_ability.setObjectName(u"comboBox_ability")
        self.comboBox_ability.setGeometry(QRect(250, 36, 150, 21))
        self.comboBox_ability.setFont(font1)
        self.comboBox_weapon = QComboBox(self.frame_game_1)
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.addItem("")
        self.comboBox_weapon.setObjectName(u"comboBox_weapon")
        self.comboBox_weapon.setGeometry(QRect(250, 56, 150, 21))
        self.comboBox_weapon.setFont(font1)
        self.comboBox_module = QComboBox(self.frame_game_1)
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.addItem("")
        self.comboBox_module.setObjectName(u"comboBox_module")
        self.comboBox_module.setGeometry(QRect(250, 76, 150, 21))
        self.comboBox_module.setFont(font1)
        self.comboBox_mode = QComboBox(self.frame_game_1)
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setObjectName(u"comboBox_mode")
        self.comboBox_mode.setGeometry(QRect(470, 36, 130, 21))
        self.comboBox_mode.setFont(font1)
        self.comboBox_map = QComboBox(self.frame_game_1)
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.addItem("")
        self.comboBox_map.setObjectName(u"comboBox_map")
        self.comboBox_map.setGeometry(QRect(470, 56, 130, 21))
        font2 = QFont()
        font2.setFamilies([u"Moon"])
        font2.setBold(False)
        self.comboBox_map.setFont(font2)
        self.comboBox_win_loss = QComboBox(self.frame_game_1)
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.addItem("")
        self.comboBox_win_loss.setObjectName(u"comboBox_win_loss")
        self.comboBox_win_loss.setGeometry(QRect(470, 76, 130, 21))
        self.comboBox_win_loss.setFont(font1)
        self.date_lineEdit = QLineEdit(self.frame_game_1)
        self.date_lineEdit.setObjectName(u"date_lineEdit")
        self.date_lineEdit.setGeometry(QRect(430, 10, 131, 22))
        self.date_lineEdit.setFont(font)
        self.lineEdit_season = QLineEdit(self.frame_game_1)
        self.lineEdit_season.setObjectName(u"lineEdit_season")
        self.lineEdit_season.setGeometry(QRect(660, 10, 88, 21))
        self.lineEdit_season.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Game Data Editor", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Game1", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"K/D:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Kills:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Deaths:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Assists:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Weapon:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Ability:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Module:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Date/Time:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Map:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"W/L:", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Season:", None))
        self.comboBox_ability.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_ability.setItemText(1, QCoreApplication.translate("MainWindow", u"Blast", None))
        self.comboBox_ability.setItemText(2, QCoreApplication.translate("MainWindow", u"Shield Healing", None))
        self.comboBox_ability.setItemText(3, QCoreApplication.translate("MainWindow", u"Teleportation", None))
        self.comboBox_ability.setItemText(4, QCoreApplication.translate("MainWindow", u"Invisibility", None))
        self.comboBox_ability.setItemText(5, QCoreApplication.translate("MainWindow", u"Flash Bang", None))
        self.comboBox_ability.setItemText(6, QCoreApplication.translate("MainWindow", u"Black Hole", None))

        self.comboBox_weapon.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_weapon.setItemText(1, QCoreApplication.translate("MainWindow", u"Sparks", None))
        self.comboBox_weapon.setItemText(2, QCoreApplication.translate("MainWindow", u"Storm", None))
        self.comboBox_weapon.setItemText(3, QCoreApplication.translate("MainWindow", u"Orion", None))
        self.comboBox_weapon.setItemText(4, QCoreApplication.translate("MainWindow", u"Pulser", None))
        self.comboBox_weapon.setItemText(5, QCoreApplication.translate("MainWindow", u"Vortex-5", None))
        self.comboBox_weapon.setItemText(6, QCoreApplication.translate("MainWindow", u"Nova", None))

        self.comboBox_module.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_module.setItemText(1, QCoreApplication.translate("MainWindow", u"Regeneration", None))
        self.comboBox_module.setItemText(2, QCoreApplication.translate("MainWindow", u"Mobility", None))
        self.comboBox_module.setItemText(3, QCoreApplication.translate("MainWindow", u"Vampirism", None))
        self.comboBox_module.setItemText(4, QCoreApplication.translate("MainWindow", u"Berserker", None))
        self.comboBox_module.setItemText(5, QCoreApplication.translate("MainWindow", u"Heal Booster", None))
        self.comboBox_module.setItemText(6, QCoreApplication.translate("MainWindow", u"Synchronisation", None))

        self.comboBox_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Backup", None))
        self.comboBox_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Q-Ball", None))
        self.comboBox_mode.setItemText(3, QCoreApplication.translate("MainWindow", u"Free for All", None))
        self.comboBox_mode.setItemText(4, QCoreApplication.translate("MainWindow", u"Ranked", None))
        self.comboBox_mode.setItemText(5, QCoreApplication.translate("MainWindow", u"Co-op vs. AIs", None))
        self.comboBox_mode.setItemText(6, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.comboBox_map.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_map.setItemText(1, QCoreApplication.translate("MainWindow", u"Trinity Island", None))
        self.comboBox_map.setItemText(2, QCoreApplication.translate("MainWindow", u"Shroomworld", None))
        self.comboBox_map.setItemText(3, QCoreApplication.translate("MainWindow", u"Lost Complex", None))
        self.comboBox_map.setItemText(4, QCoreApplication.translate("MainWindow", u"Twilight Path", None))
        self.comboBox_map.setItemText(5, QCoreApplication.translate("MainWindow", u"Singularity", None))

        self.comboBox_win_loss.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_win_loss.setItemText(1, QCoreApplication.translate("MainWindow", u"Win", None))
        self.comboBox_win_loss.setItemText(2, QCoreApplication.translate("MainWindow", u"loss", None))
        self.comboBox_win_loss.setItemText(3, QCoreApplication.translate("MainWindow", u"Draw", None))

        self.date_lineEdit.setText(QCoreApplication.translate("MainWindow", u"", None))
    # retranslateUi

# The Window for editing game data
class GameDataEditor(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None, game_name=None, season=None, main_window=None, get_next_game_number=None, rename_games=None, load_saved_games=None):
        super(GameDataEditor, self).__init__(parent)
        
        self.load_saved_games = load_saved_games
        self.get_next_game_number = get_next_game_number
        self.rename_games = rename_games
        
        # Create an instance of the Ui_MainWindow for the secondary window
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

        # Store the game name and season for later use
        self.game_name = game_name
        self.season = season
        self.main_window = main_window

        # Connect the "Save" button to the save functionality
        self.ui.pushButton_delete.setText("Save")  # Renamed as "Save"
        self.ui.pushButton_delete.clicked.connect(self.save_game_data)

        # Load existing game data into the form fields
        self.load_game_data()

    def load_game_data(self):
        # Load the game data from the JSON file
        with open(BASE_DIR, "r") as jsonfile:
            data = json.load(jsonfile)

        # Check if the game exists in the specified season
        if self.season not in data or self.game_name not in data[self.season]:
            return  # Handle the error as needed (e.g., show a message to the user)

        # Get the specific game data
        game_data = data[self.season][self.game_name]

        # Populate the fields in the editor window with game data
        self.ui.spinBox_kills.setValue(int(game_data['Kills']))
        self.ui.spinBox_deaths.setValue(int(game_data['Deaths']))
        self.ui.spinBox_assists.setValue(int(game_data['Assists']))
        self.ui.comboBox_ability.setCurrentText(game_data['Ability'])
        self.ui.comboBox_weapon.setCurrentText(game_data['Weapon'])
        self.ui.comboBox_module.setCurrentText(game_data['Module'])
        self.ui.comboBox_mode.setCurrentText(game_data['Mode'])
        self.ui.comboBox_map.setCurrentText(game_data['Map'])
        self.ui.comboBox_win_loss.setCurrentText(game_data['Win/Loss'])
        self.ui.date_lineEdit.setText(game_data['DateTime'])


    def save_game_data(self):
        # Load the existing data from the JSON file
        with open(BASE_DIR, "r") as jsonfile:
            data = json.load(jsonfile)

        # Get the new season from the lineEdit_season
        new_season = self.ui.lineEdit_season.text()

        # Check if the new season exists in the data; if not, create it
        if new_season not in data:
            data[new_season] = {}

        # Move the game data to the new season
        if self.season in data and self.game_name in data[self.season]:
            # Get the game data from the old season
            game_data = data[self.season][self.game_name]

            # Check for existing game names in the new season
            existing_game_names = data[new_season].keys()
            new_game_name = self.game_name

            # Generate a unique game name if necessary
            if new_game_name in existing_game_names:
                new_game_name = f"Game{self.get_next_game_number(data[new_season], 'Game')}"

            # Prepare the updated game data
            updated_game_data = {
                "DateTime": self.ui.date_lineEdit.text(),
                "Kills": self.ui.spinBox_kills.value(),
                "Deaths": self.ui.spinBox_deaths.value(),
                "Assists": self.ui.spinBox_assists.value(),
                "Ability": self.ui.comboBox_ability.currentText(),
                "Weapon": self.ui.comboBox_weapon.currentText(),
                "Module": self.ui.comboBox_module.currentText(),
                "Mode": self.ui.comboBox_mode.currentText(),
                "Map": self.ui.comboBox_map.currentText(),
                "Win/Loss": self.ui.comboBox_win_loss.currentText(),
                "Timestamp": datetime.now().timestamp()
            }

            # Add the game data to the new season under the new game name
            data[new_season][new_game_name] = updated_game_data

            # Remove the game data from the old season
            del data[self.season][self.game_name]

        # Save the updated data back to the JSON file
        with open(BASE_DIR, "w") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        # Call the rename_games method for both the old and new seasons
        if self.main_window:
            self.main_window.rename_games(self.season)  # Rename games in the old season
            self.main_window.rename_games(new_season)    # Rename games in the new season

        self.load_saved_games()
        self.close()  # Close the editor after saving

# The Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Load settings from the settings file and store them in self.settings
        self.settings = self.load_settings()
        
        # Apply settings to the toggle button
        self.ui.toggle_1.setChecked(self.settings['Settings']['Setting_1'])  # Set toggle based on the saved state
        
        # Connect the toggle button to toggle the setting
        self.ui.toggle_1.clicked.connect(self.toggle_setting)

        # Connect the tab change signal to the method
        self.ui.tabWidget.currentChanged.connect(self.on_tab_change)
        
        # Connect the button click event to the save_game_data method
        self.ui.pushButton_save_game.clicked.connect(self.save_game_data)
        self.ui.pushButton_reset.clicked.connect(self.reset_fields)
        
        # Connect the buttons on the Analytics tab
        self.ui.button1.clicked.connect(lambda: self.button_clicked(1))  # All game modes
        self.ui.button2.clicked.connect(lambda: self.button_clicked(2))  # Backup
        self.ui.button3.clicked.connect(lambda: self.button_clicked(3))  # Q-Ball
        self.ui.button4.clicked.connect(lambda: self.button_clicked(4))  # Free For All
        self.ui.button5.clicked.connect(lambda: self.button_clicked(5))  # Ranked
        
        # Connect the ComboBox for the statistic on the Analytics tab
        self.ui.statistic_box.currentIndexChanged.connect(self.statistic_changed)
        
        # Connect the ComboBox for the time filter on the Analytics tab
        self.ui.time_box.currentIndexChanged.connect(self.time_filter_changed)
        
        self.ui.design_2_ComboBox_Weapon.currentIndexChanged.connect(self.design_2_ComboBox_Weapon_changed)
        self.ui.design_2_ComboBox_Ability.currentIndexChanged.connect(self.design_2_ComboBox_Ability_changed)
        self.ui.design_2_ComboBox_Module.currentIndexChanged.connect(self.design_2_ComboBox_Module_changed)
        self.ui.design_2_ComboBox_Map.currentIndexChanged.connect(self.design_2_ComboBox_Map_changed)
        
        # Initialize default selections
        self.selected_statistic = 0     # Default statistic (Kills)
        self.selected_time_filter = 0   # Default time filter (Last Year)
        self.selected_button = 1        # Default button (All Game Modes)
        
        # Load graph for the first time
        self.load_graph()
        
    def load_settings(self):
        with open(SETTINGS_FILE, "r") as json_file:
            return json.load(json_file)  

    def save_settings(self):
        with open(SETTINGS_FILE, "w") as json_file:
            json.dump(self.settings, json_file, indent=4)

    def toggle_setting(self):
        # Toggle the setting value based on the current state of the toggle button
        current_value = self.ui.toggle_1.isChecked()  # Get the current state of the toggle button
        self.settings['Settings']['Setting_1'] = current_value

        # Save the updated settings back to the file
        self.save_settings()

    def load_json_data(self):
        with open(JSON_FILE, "r") as json_file:
            return json.load(json_file)
        
    def design_2_ComboBox_Weapon_changed(self):
        weapon = self.ui.design_2_ComboBox_Weapon.currentText().strip().lower()
        self.ui.design_2_tab_1_text.setText(weapon)
        
        game_data = self.load_json_data()
        
        total_kills = 0
        total_deaths = 0
        total_games = 0
        total_wins = 0
        total_losses = 0
        
        for season, games in game_data.items():
            for game_id, game in games.items():
                if game['Weapon'].strip().lower() == weapon:
                    total_kills += game['Kills']
                    total_deaths += game['Deaths']
                    total_games += 1
                    if game['Win/Loss'].strip() == "Win":
                        total_wins += 1
                    else:
                        total_losses += 1
                        
        kd_ratio = total_kills / max(1, total_deaths)
        win_rate = (total_wins / max(1, total_games)) * 100
        
        self.ui.design_2_tab_1_kd.setText(f"K/D: {kd_ratio:.2f}")
        self.ui.design_2_tab_1_kd_progress.setValue(int((total_kills / max(1, (total_kills + total_deaths))) * 100))
        self.ui.design_2_tab_1_kd_progress.setFormat(f"K/D: {kd_ratio:.2f}")
        
        self.ui.design_2_tab_1_usage.setText(f"Usage: {total_games}")
        self.ui.design_2_tab_1_usage_progress.setValue(int(win_rate))
        self.ui.design_2_tab_1_usage_progress.setFormat(f"Win Rate: {win_rate:.2f}%")
        
        self.ui.design_2_tab_1_kills_label.setText(f"K: {total_kills}")
        self.ui.design_2_tab_1_deaths_label.setText(f"D: {total_deaths}")
        
        self.ui.design_2_tab_1_wins_label.setText(f"W: {total_wins}")
        self.ui.design_2_tab_1_losses_label.setText(f"L: {total_losses}")
        
    def design_2_ComboBox_Ability_changed(self):
        ability = self.ui.design_2_ComboBox_Ability.currentText().strip().lower()
        self.ui.design_2_tab_3_text.setText(ability)
        
        game_data = self.load_json_data()
        
        total_games = 0
        total_wins = 0
        total_losses = 0
        
        for season, games in game_data.items():
            for game_id, game in games.items():
                if game['Ability'].strip().lower() == ability:
                    total_games += 1
                    if game['Win/Loss'].strip() == "Win":
                        total_wins += 1
                    else:
                        total_losses += 1
        
        win_rate = (total_wins / max(1, total_games)) * 100
        
        self.ui.design_2_tab_3_usage.setText(f"Usage: {total_games}")
        self.ui.design_2_tab_3_usage_progress.setValue(int(win_rate))
        self.ui.design_2_tab_3_usage_progress.setFormat(f"Win Rate: {win_rate:.2f}%")
        
        self.ui.design_2_tab_3_wins_label.setText(f"W: {total_wins}")
        self.ui.design_2_tab_3_losses_label.setText(f"L: {total_losses}")
        
    def design_2_ComboBox_Module_changed(self):
        module = self.ui.design_2_ComboBox_Module.currentText().strip().lower()
        self.ui.design_2_tab_2_text.setText(module)
        
        game_data = self.load_json_data()
        
        total_games = 0
        total_wins = 0
        total_losses = 0
        
        for season, games in game_data.items():
            for game_id, game in games.items():
                if game['Module'].strip().lower() == module:
                    total_games += 1
                    if game['Win/Loss'].strip() == "Win":
                        total_wins += 1
                    else:
                        total_losses += 1
        
        win_rate = (total_wins / max(1, total_games)) * 100
        
        self.ui.design_2_tab_2_usage.setText(f"Usage: {total_games}")
        self.ui.design_2_tab_2_usage_progress.setValue(int(win_rate))
        self.ui.design_2_tab_2_usage_progress.setFormat(f"Win Rate: {win_rate:.2f}%")
        
        self.ui.design_2_tab_2_wins_label.setText(f"W: {total_wins}")
        self.ui.design_2_tab_2_losses_label.setText(f"L: {total_losses}")
        
    def design_2_ComboBox_Map_changed(self):
        map = self.ui.design_2_ComboBox_Map.currentText().strip().lower()
        self.ui.design_2_tab_4_text.setText(map)
        
        game_data = self.load_json_data()
        
        total_kills = 0
        total_deaths = 0
        total_games = 0
        total_wins = 0
        total_losses = 0
        
        for season, games in game_data.items():
            for game_id, game in games.items():
                if game['Map'].strip().lower() == map:
                    total_kills += game['Kills']
                    total_deaths += game['Deaths']
                    total_games += 1
                    if game['Win/Loss'].strip() == "Win":
                        total_wins += 1
                    else:
                        total_losses += 1
        
        kd_ratio = total_kills / max(1, total_deaths)
        win_rate = (total_wins / max(1, total_games)) * 100
        
        self.ui.design_2_tab_4_kd.setText(f"K/D: {kd_ratio:.2f}")
        self.ui.design_2_tab_4_kd_progress.setValue(int((total_kills / max(1, (total_kills + total_deaths))) * 100))
        self.ui.design_2_tab_4_kd_progress.setFormat(f"K/D: {kd_ratio:.2f}")
        
        self.ui.design_2_tab_4_usage.setText(f"Played: {total_games}")
        self.ui.design_2_tab_4_usage_progress.setValue(int(win_rate))
        self.ui.design_2_tab_4_usage_progress.setFormat(f"Win Rate: {win_rate:.2f}%")
        
        self.ui.design_2_tab_4_kills_label.setText(f"K: {total_kills}")
        self.ui.design_2_tab_4_deaths_label.setText(f"D: {total_deaths}")
        
        self.ui.design_2_tab_4_wins_label.setText(f"W: {total_wins}")
        self.ui.design_2_tab_4_losses_label.setText(f"L: {total_losses}")

    def filter_data_by_mode(self, games):
        if self.selected_button == 1:   # Button 1 -> All modes
            return games
        mode_mapping = {
            2: "Backup",                # Button 2 -> Backup
            3: "Q-Ball",                # Button 3 -> Q-Ball
            4: "Free for All",          # Button 4 -> Free For All
            5: "Ranked"                 # Button 5 -> Ranked
        }
        return {
            game_id: data for game_id, data in games.items()
            if data['Mode'].strip().lower() == mode_mapping[self.selected_button].lower()
        }

    def get_statistic_values(self, filtered_data, x_labels):
        y_values = [0] * len(x_labels)  # Initialize Y-values as zeros for each X-axis label

        # Iterate through the filtered data and calculate stats per X-axis label
        for game_id, game_data in filtered_data.items():
            game_datetime = datetime.strptime(game_data['DateTime'], '%Y-%m-%d %H:%M')
            game_label = game_datetime.strftime('%b') if self.selected_time_filter == 0 else game_datetime.strftime('%d.%m')

            if game_label in x_labels:
                index = x_labels.index(game_label)
                
                if self.selected_statistic == 0:  # K/D
                    total_kills = 0
                    total_deaths = 0
                    for game_id, game_data in filtered_data.items():
                        game_datetime = datetime.strptime(game_data['DateTime'], '%Y-%m-%d %H:%M')
                        game_label = game_datetime.strftime('%b') if self.selected_time_filter == 0 else game_datetime.strftime('%d.%m')
                        if game_label == x_labels[index]:
                            total_kills += game_data['Kills']
                            total_deaths += game_data['Deaths']
                    if total_deaths > 0:
                        y_values[index] = total_kills / total_deaths
                    else:
                        y_values[index] = 0
                elif self.selected_statistic == 1:  # Kills
                    y_values[index] += game_data['Kills']
                elif self.selected_statistic == 2:  # Deaths
                    y_values[index] += game_data['Deaths']
                elif self.selected_statistic == 3:  # Matches
                    y_values[index] += 1
                elif self.selected_statistic == 4:  # Wins
                    y_values[index] += 1 if game_data['Win/Loss'].strip().lower() == 'win' else 0
                elif self.selected_statistic == 5:  # Losses
                    y_values[index] += 1 if game_data['Win/Loss'].strip().lower() == 'loss' else 0
                elif self.selected_statistic == 6:  # Win%
                    games_in_label = [
                        game for game in filtered_data.values()
                        if datetime.strptime(game['DateTime'], '%Y-%m-%d %H:%M').strftime('%b' if self.selected_time_filter == 0 else '%d.%m') == game_label
                    ]

                    if games_in_label:  # If there are games in this period
                        wins_in_label = sum(1 for game in games_in_label if game['Win/Loss'].strip().lower() == 'win')
                        total_games_in_label = len(games_in_label)
                        win_percentage = (wins_in_label / total_games_in_label) * 100
                        y_values[index] = win_percentage  # Set the Win% for this specific period (label)

        return y_values

    def button_clicked(self, index):
        # Reset all buttons to white
        for i in range(1, 6):
            getattr(self.ui, f"button{i}").setStyleSheet("color: white")
        
        # Set the clicked button to purple
        getattr(self.ui, f"button{index}").setStyleSheet("color: purple")
        
        # Store the selected mode (button clicked)
        self.selected_button = index

        # Re-load graph with updated mode
        self.load_graph()

    def statistic_changed(self, statistic):
        self.selected_statistic = statistic

        # Re-load graph with updated statistic
        self.load_graph()

    def time_filter_changed(self, time_filter):
        self.selected_time_filter = time_filter
   
        # Re-load graph with updated time filter
        self.load_graph()

    def filter_data_by_time(self, games):
        now = datetime.now()

        if self.selected_time_filter == 0:      # Last Year / 12 months
            cutoff = now - timedelta(days=365)
            x_values = [(now - timedelta(days=365 - i*30)).strftime('%b') for i in range(12)]
        elif self.selected_time_filter == 1:    # Last Month / 30 days
            cutoff = now - timedelta(days=30)
            x_values = [(now - timedelta(days=i)).strftime('%d.%m') for i in range(30)]
        elif self.selected_time_filter == 2:    # Last Week / 7 days
            cutoff = now - timedelta(days=7)
            x_values = [(now - timedelta(days=i)).strftime('%d.%m') for i in range(7)]

        # Filter games by comparing the DateTime field to the cutoff
        filtered_games = {}
        for game_id, game_data in games.items():
            game_datetime = datetime.strptime(game_data['DateTime'], '%Y-%m-%d %H:%M')
            if game_datetime > cutoff:
                filtered_games[game_id] = game_data

        return filtered_games, x_values

    def load_graph(self):
        # Clear the existing graph before plotting the new one
        self.ui.graph.clear()

        # Load and filter data from the JSON file
        data = self.load_json_data()

        # Combine the filters to get the final dataset
        filtered_data = {}
        x_labels = []  # X-axis labels that we'll display
        for season, games in data.items():
            season_games, season_x_values = self.filter_data_by_time(games)
            season_games = self.filter_data_by_mode(season_games)
            filtered_data.update(season_games)
            x_labels = season_x_values  # Use the last calculated x_values for graph

        # Get the y values for the graph based on the filtered data
        y_values = self.get_statistic_values(filtered_data, x_labels)

        # Reverse both the X-axis labels and the Y-values to match the inverted X-axis
        x_labels.reverse()
        y_values.reverse()

        # Plot the data on the graph (fill gaps where no data is available)
        pen = pg.mkPen('purple')
        x_indices = list(range(len(x_labels)))
        self.ui.graph.plot(x_indices, y_values, pen=pen, symbol='x')

        # Set the X-axis with custom labels (e.g., months or dates)
        x_axis = self.ui.graph.getAxis('bottom')
        x_axis.setTicks([[(i, label) for i, label in enumerate(x_labels)]])

        # Set fixed limits and range for the graph
        y_min, y_max = min(y_values), max(y_values)
        self.ui.graph.setLimits(xMin=0, xMax=len(x_labels) - 1, yMin=0, yMax=y_max)

        # Disable mouse dragging or zooming on the graph
        self.ui.graph.setMouseEnabled(x=False, y=False)

        # Set the fixed range for the view
        self.ui.graph.setRange(xRange=(0, len(x_labels) - 1), yRange=(0, y_max))

    def on_tab_change(self, index):
        if index == 3:
            # Call load_saved_games only if the game_data.json file exists
            if BASE_DIR.exists():
                self.load_saved_games()
        
        if index == 2:
            # Call load_general_stats only if the game_data.json file exists
            if BASE_DIR.exists():
                self.load_general_stats()
                
        if index == 4:
            # checks what setting is enabled
            if self.settings['Settings']['Setting_1']:
                self.ui.design_2.show()
                self.ui.design_1.hide()
                self.ui.filler.setMinimumSize(796, 1070)
            else:
                self.ui.design_2.hide()
                self.ui.design_1.show()
                self.ui.design_1.setMinimumHeight(5980)
                self.ui.filler.setMinimumHeight(6540)
                self.load_specific_stats()
                
    def load_specific_stats(self):
        # Load data using the existing load_json_data function
        game_data = self.load_json_data()

        # Predefined lists for weapons, modules, abilities, and maps
        weapon_list = ["Sparks", "Storm", "Orion", "Pulser", "Vortex-5", "Nova"]
        module_list = ["Regeneration", "Mobility", "Vampirism", "Berserker", "Heal Booster", "Synchronisation"]
        ability_list = ["Blast", "Shield Healing", "Teleportation", "Invisibility", "Flash Bang", "Black Hole"]
        map_list = ["Trinity Island", "Shroomworld", "Lost Complex", "Twilight Path", "Singularity"]

        # Initialize empty dicts for each category
        weapons = {weapon: {'Kills': 0, 'Deaths': 0, 'Wins': 0, 'Losses': 0, 'Total_Uses': 0} for weapon in weapon_list}
        modules = {module: {'Wins': 0, 'Losses': 0, 'Total_Uses': 0} for module in module_list}
        abilities = {ability: {'Wins': 0, 'Losses': 0, 'Total_Uses': 0} for ability in ability_list}
        maps = {game_map: {'Kills': 0, 'Deaths': 0, 'Wins': 0, 'Losses': 0, 'Total_Uses': 0} for game_map in map_list}

        # Collect and aggregate data from game_data
        for season, games in game_data.items():
            for game_id, game_data in games.items():
                # Update weapon stats
                weapon = game_data['Weapon'].strip()
                if weapon in weapons:
                    weapons[weapon]['Kills'] += game_data['Kills']
                    weapons[weapon]['Deaths'] += game_data['Deaths']
                    weapons[weapon]['Wins'] += 1 if game_data['Win/Loss'].strip().lower() == 'win' else 0
                    weapons[weapon]['Losses'] += 1 if game_data['Win/Loss'].strip().lower() == 'loss' else 0
                    weapons[weapon]['Total_Uses'] += 1

                # Update module stats (no kills/deaths)
                module = game_data['Module'].strip()
                if module in modules:
                    modules[module]['Wins'] += 1 if game_data['Win/Loss'].strip().lower() == 'win' else 0
                    modules[module]['Losses'] += 1 if game_data['Win/Loss'].strip().lower() == 'loss' else 0
                    modules[module]['Total_Uses'] += 1

                # Update ability stats (no kills/deaths)
                ability = game_data['Ability'].strip()
                if ability in abilities:
                    abilities[ability]['Wins'] += 1 if game_data['Win/Loss'].strip().lower() == 'win' else 0
                    abilities[ability]['Losses'] += 1 if game_data['Win/Loss'].strip().lower() == 'loss' else 0
                    abilities[ability]['Total_Uses'] += 1

                # Update map stats
                game_map = game_data['Map'].strip()
                if game_map in maps:
                    maps[game_map]['Kills'] += game_data['Kills']
                    maps[game_map]['Deaths'] += game_data['Deaths']
                    maps[game_map]['Wins'] += 1 if game_data['Win/Loss'].strip().lower() == 'win' else 0
                    maps[game_map]['Losses'] += 1 if game_data['Win/Loss'].strip().lower() == 'loss' else 0
                    maps[game_map]['Total_Uses'] += 1

        # Find the best items based on Kills for weapons and maps, Wins for modules and abilities
        best_weapon = max(weapons, key=lambda w: weapons[w]['Kills'])
        best_module = max(modules, key=lambda m: modules[m]['Wins'])
        best_ability = max(abilities, key=lambda a: abilities[a]['Wins'])
        best_map = max(maps, key=lambda m: maps[m]['Kills'])

        # Create UI containers
        y_offset = 10  # Start position for dynamically created boxes

        # Show the best items first
        self.create_ui_containers({best_weapon: weapons[best_weapon]}, "Weapon", best_weapon, y_offset)
        y_offset += 260
        self.create_ui_containers({best_module: modules[best_module]}, "Module", best_module, y_offset)
        y_offset += 260
        self.create_ui_containers({best_ability: abilities[best_ability]}, "Ability", best_ability, y_offset)
        y_offset += 260
        self.create_ui_containers({best_map: maps[best_map]}, "Map", best_map, y_offset)
        y_offset += 260

        # Show the rest of the items
        for item_dict, item_type, best_item in [
            (weapons, "Weapon", best_weapon),
            (modules, "Module", best_module),
            (abilities, "Ability", best_ability),
            (maps, "Map", best_map)
        ]:
            # Remove the best item so we don't show it twice
            del item_dict[best_item]
            self.create_ui_containers(item_dict, item_type, best_item, y_offset)
            y_offset += len(item_dict) * 260

    def create_ui_containers(self, items, item_type, best_item, y_offset):
        box_height = 260  # Height of each box
        
        # Mappings for image file names
        weapon_images = {
            "Storm": "Weapon_Pounder.png",
            "Nova": "Weapon_Ransacker.png",
            "Orion": "Weapon_Revoker.png",
            "Sparks": "Weapon_Sparkler.png",
            "Vortex-5": "Weapon_Spreader.png",
            "Pulser": "Weapon_Striker.png"
        }
        
        module_images = {
            "Berserker": "Module_Berzerker.png",
            "Heal Booster": "Module_HealBooster.png",
            "Mobility": "Module_Mobility.png",
            "Regeneration": "Module_Regeneration.png",
            "Synchronisation": "Module_Synchronisation.png",
            "Vampirism": "Module_Vampirism.png"
        }
        
        ability_images = {
            "Black Hole": "Ability_BlackHole.png",
            "Blast": "Ability_Blast.png",
            "Flash Bang": "Ability_Flash.png",
            "Shield Healing": "Ability_Heal.png",
            "Invisibility": "Ability_Invisibility.png",
            "Teleportation": "Ability_Teleport.png"
        }
        
        map_images = {
            "Trinity Island": "Trinity_Island_02.jpg",
            "Shroomworld": "Shroomworld_02.jpg",
            "Lost Complex": "Lost_Complex_02.jpg",
            "Twilight Path": "Twilight_Path_02.jpg",
            "Singularity": "Blette.png"
        }

        for item_name, stats in items.items():
            # Clone the template for the design_1_box
            item_box = QGroupBox(self.ui.design_1)  # Clone the design_1_box
            item_box.setGeometry(QRect(10, y_offset, 755, 240))
            item_box.setObjectName(f"{item_type.lower()}_{item_name}")

            # Image
            item_image = QLabel(item_box)
            
            # Set the correct image based on item type and name, considering folder paths
            if item_type == "Weapon":
                item_image.setGeometry(QRect(10, 10, 120, 120))
                image_path = weapon_images.get(item_name, "default.png")
                item_image.setPixmap(QPixmap(f"assets/Weapon/{image_path}"))
            elif item_type == "Module":
                item_image.setGeometry(QRect(10, 10, 120, 120))
                image_path = module_images.get(item_name, "default.png")
                item_image.setPixmap(QPixmap(f"assets/Module/{image_path}"))
            elif item_type == "Ability":
                item_image.setGeometry(QRect(10, 10, 120, 120))
                image_path = ability_images.get(item_name, "default.png")
                item_image.setPixmap(QPixmap(f"assets/Ability/{image_path}"))
            elif item_type == "Map":
                item_image.setGeometry(QRect(10, 10, 150, 110))
                image_path = map_images.get(item_name, "default.jpg")
                if item_name == "Singularity":
                    item_image.setPixmap(QPixmap(f"assets/{image_path}"))
                else:
                    item_image.setPixmap(QPixmap(f"assets/Arenas/{image_path}"))
                
            item_image.setScaledContents(True)

            # Name Label
            name_label = QLabel(item_box)
            name_label.setGeometry(QRect(130, 15, 300, 30))
            name_label.setFont(QFont("Moon", 22))
            name_label.setText(item_name)
            name_label.setAlignment(Qt.AlignCenter)

            # If it's a weapon or map, show K/D label, otherwise skip it
            if item_type in ["Weapon", "Map"]:
                # K/D Label
                kd_label = QLabel(item_box)
                kd_label.setGeometry(QRect(280, 160, 300, 30))
                kd_label.setFont(QFont("Moon", 16))
                kd_label.setText(f"K/D: {stats['Kills'] / max(1, stats['Deaths']):.2f}")
                
                # Kills Label
                kills_label = QLabel(item_box)
                kills_label.setGeometry(QRect(280, 200, 300, 30))
                kills_label.setFont(QFont("Moon", 16))
                kills_label.setText(f"Kills: {stats['Kills']}")

            # Wins/Loss Label
            win_loss_label = QLabel(item_box)
            win_loss_label.setGeometry(QRect(20, 160, 300, 30))
            win_loss_label.setFont(QFont("Moon", 16))
            win_loss_label.setText(f"W/L: {stats['Wins']}/{stats['Losses']}")

            # Total Uses Label
            total_uses_label = QLabel(item_box)
            total_uses_label.setGeometry(QRect(20, 200, 300, 30))
            total_uses_label.setFont(QFont("Moon", 16))
            total_uses_label.setText(f"Total Uses: {stats['Total_Uses']}")

            # Circular Progress Bar for Winrate
            circular_progress_bar_container = QFrame(item_box)
            circular_progress_bar_container.setGeometry(QRect(510, 10, 220, 220))

            layout = QVBoxLayout()
            circular_progress_bar = CircularProgress()
            circular_progress_bar.value = int((stats['Wins'] / max(1, stats['Wins'] + stats['Losses'])) * 100)
            circular_progress_bar.prefix = "Winrate: "
            circular_progress_bar.text_color = "#FFFFFF"
            circular_progress_bar.progress_width = 2
            circular_progress_bar.progress_color = "purple"
            circular_progress_bar.font_family = "Moon"
            circular_progress_bar.font_size = 18
            circular_progress_bar.height = 200
            circular_progress_bar.width = 200
            circular_progress_bar.setMinimumSize(circular_progress_bar.width, circular_progress_bar.height)

            layout.addWidget(circular_progress_bar, Qt.AlignCenter, Qt.AlignCenter)
            circular_progress_bar_container.setLayout(layout)

            # Highlight best item with a golden border
            if item_name == best_item:
                item_box.setStyleSheet("border: 1px solid gold;")
                circular_progress_bar.progress_color = "gold"
                item_image.setStyleSheet("border: none;")
                name_label.setStyleSheet("border: none; color: gold;")
                if item_type in ["Weapon", "Map"]:
                    kd_label.setStyleSheet("border: none;")
                    kills_label.setStyleSheet("border: none;")
                win_loss_label.setStyleSheet("border: none;")
                total_uses_label.setStyleSheet("border: none;")
                circular_progress_bar_container.setStyleSheet("border: none;")

            # Adjust the vertical offset for the next box
            y_offset += box_height

            # Show the item box
            item_box.show()
        
    def load_general_stats(self):
        # First, calculate all general stats
        self.calculate_general_stats()

        # Update the general statistics UI
        self.ui.lifetime_kd_lable_general.setText(f"Lifetime K/D: {self.kd_ratio}")
        self.ui.avg_kills_lable_general.setText(f"Avg. Kills: {round(self.total_kills / max(1, self.total_games), 2)}")
        self.ui.kills_lable_general.setText(f"Kills: {self.total_kills}")
        self.ui.deaths_lable_general.setText(f"Deaths: {self.total_deaths}")
        self.ui.assists_lable_general.setText(f"Assists: {self.total_assists}")
        self.ui.matches_lable_general.setText(f"Matches: {self.total_games}")
        self.ui.wins_lable_general.setText(f"Wins: {self.total_wins}")
        self.ui.losses_lable_general.setText(f"Losses: {self.total_losses}")
        self.ui.lifetime_win_ration_lable_general.setText(f"Lifetime W/L: {self.win_ratio}%")
        self.ui.progressBar_win_ratio_general.setValue(self.win_ratio)
        self.ui.progressBar_win_ratio_general.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: black;} QProgressBar::chunk { background-color: purple;}")
        self.ui.most_used_ability_lable_general.setText(f"Most Used Ability: {self.most_used_ability}")
        self.ui.most_used_weapon_lable_general.setText(f"Most Used Weapon: {self.most_used_weapon}")
        self.ui.most_used_module_lable_general.setText(f"Most Used Module: {self.most_used_module}")
        self.ui.best_map_lable_general.setText(f"Best Map: {self.best_map}")
        self.ui.best_mode_lable_general.setText(f"Best Mode: {self.best_mode}")
        self.ui.best_weapon_lable_general.setText(f"Best Weapon: {self.best_weapon}")

        # Clear previous seasonal stats if any, but keep the general stats
        for i in reversed(range(self.ui.verticalLayout_2.count())): 
            widget = self.ui.verticalLayout_2.itemAt(i).widget()
            if widget is not None and widget.objectName() != "general_statistics":
                widget.deleteLater()

        # Load the data from the JSON file
        if not BASE_DIR.exists():
            return

        with open(BASE_DIR, "r") as json_file:
            data = json.load(json_file)

        # Loop through each season and create a group box for it
        for season, games in data.items():
            season_group_box = self.create_season_group_box(season, games)
            self.ui.verticalLayout_2.addWidget(season_group_box)

    def create_season_group_box(self, season, games):
        # Create a group box for the season with the same dimensions and settings
        season_group_box = QGroupBox(f"Season: {season}")
        season_group_box.setMinimumSize(QSize(0, 300))
        season_group_box.setMaximumSize(QSize(16777215, 300))

        # Set the font for the season group box
        font = QFont()
        font.setFamily("Moon")
        font.setPointSize(16)
        season_group_box.setFont(font)

        # Initialize the layout within the season group box
        total_kills = 0
        total_deaths = 0
        total_assists = 0
        total_wins = 0
        total_losses = 0
        total_games = 0
        ability_counter = Counter()
        weapon_counter = Counter()
        module_counter = Counter()
        map_wins = Counter()
        mode_wins = Counter()

        # Loop through each game and accumulate stats
        for game_id, game_data in games.items():
            total_kills += game_data["Kills"]
            total_deaths += game_data["Deaths"]
            total_assists += game_data["Assists"]
            total_games += 1

            # Count wins and losses
            if game_data["Win/Loss"].strip().lower() == "win":
                total_wins += 1
                map_wins[game_data["Map"].strip()] += 1
                mode_wins[game_data["Mode"].strip()] += 1
            elif game_data["Win/Loss"].strip().lower() == "loss":
                total_losses += 1

            # Count abilities, weapons, and modules usage
            ability_counter[game_data["Ability"].strip()] += 1
            weapon_counter[game_data["Weapon"].strip()] += 1
            module_counter[game_data["Module"].strip()] += 1

        # Avoid division by zero
        kd_ratio = round(total_kills / max(1, total_deaths), 2)
        win_ratio = round((total_wins / max(1, total_games)) * 100, 2)

        # Determine most used items and best performance metrics
        most_used_ability = ability_counter.most_common(1)[0][0] if ability_counter else "None"
        most_used_weapon = weapon_counter.most_common(1)[0][0] if weapon_counter else "None"
        most_used_module = module_counter.most_common(1)[0][0] if module_counter else "None"
        best_map = map_wins.most_common(1)[0][0] if map_wins else "None"
        best_mode = mode_wins.most_common(1)[0][0] if mode_wins else "None"
        best_weapon = most_used_weapon  # You can replace this with logic for "best" weapon if needed

        # Manually position and size the labels and progress bar
        lifetime_kd_label = QLabel(f"K/D Ratio: {kd_ratio}", season_group_box)
        lifetime_kd_label.setGeometry(QRect(10, 20, 200, 31))

        lifetime_win_ratio_label = QLabel(f"W/L Ratio: {win_ratio}%", season_group_box)
        lifetime_win_ratio_label.setGeometry(QRect(240, 20, 230, 31))
        
        avg_kills_label = QLabel(f"Avg. Kills: {round(total_kills / max(1, total_games), 2)}", season_group_box)
        avg_kills_label.setGeometry(QRect(10, 50, 261, 31))

        progressBar_win_ratio = QProgressBar(season_group_box)
        progressBar_win_ratio.setGeometry(QRect(480, 34, 261, 2))
        progressBar_win_ratio.setValue(win_ratio)
        progressBar_win_ratio.setTextVisible(False)
        progressBar_win_ratio.setStyleSheet("QProgressBar { border-radius: 10px; text-align: center; background-color: black;} QProgressBar::chunk { background-color: purple;}")

        kills_label = QLabel(f"Kills: {total_kills}", season_group_box)
        kills_label.setGeometry(QRect(10, 80, 200, 31))

        deaths_label = QLabel(f"Deaths: {total_deaths}", season_group_box)
        deaths_label.setGeometry(QRect(10, 110, 200, 31))

        assists_label = QLabel(f"Assists: {total_assists}", season_group_box)
        assists_label.setGeometry(QRect(10, 140, 200, 31))

        wins_label = QLabel(f"Wins: {total_wins}", season_group_box)
        wins_label.setGeometry(QRect(240, 50, 200, 31))

        losses_label = QLabel(f"Losses: {total_losses}", season_group_box)
        losses_label.setGeometry(QRect(240, 80, 200, 31))

        matches_label = QLabel(f"Matches: {total_games}", season_group_box)
        matches_label.setGeometry(QRect(240, 110, 200, 31))

        # Add most used ability, weapon, and module
        most_used_ability_label = QLabel(f"Most Used Ability: {most_used_ability}", season_group_box)
        most_used_ability_label.setGeometry(QRect(10, 200, 420, 31))

        most_used_weapon_label = QLabel(f"Most Used Weapon: {most_used_weapon}", season_group_box)
        most_used_weapon_label.setGeometry(QRect(10, 230, 420, 31))

        most_used_module_label = QLabel(f"Most Used Module: {most_used_module}", season_group_box)
        most_used_module_label.setGeometry(QRect(10, 260, 420, 31))

        # Add best map, mode, and weapon labels
        best_map_label = QLabel(f"Best Map: {best_map}", season_group_box)
        best_map_label.setGeometry(QRect(440, 260, 300, 31))

        best_mode_label = QLabel(f"Best Mode: {best_mode}", season_group_box)
        best_mode_label.setGeometry(QRect(440, 200, 300, 31))

        best_weapon_label = QLabel(f"Best Weapon: {best_weapon}", season_group_box)
        best_weapon_label.setGeometry(QRect(440, 230, 300, 31))

        return season_group_box  # Ensure the group box is returned

    def calculate_general_stats(self):
        # Initialize all counters
        self.total_kills = 0
        self.total_deaths = 0
        self.total_assists = 0
        self.total_wins = 0
        self.total_losses = 0
        self.total_games = 0
        ability_counter = Counter()
        weapon_counter = Counter()
        module_counter = Counter()
        map_wins = Counter()
        mode_wins = Counter()
        weapon_kd_ratio = {}

        # Load the data from the JSON file
        if not BASE_DIR.exists():
            return

        with open(BASE_DIR, "r") as json_file:
            data = json.load(json_file)

        # Loop through each season
        for season, games in data.items():
            # Loop through each game in the season
            for game_id, game_data in games.items():
                # Aggregate basic stats
                self.total_kills += game_data["Kills"]
                self.total_deaths += game_data["Deaths"]
                self.total_assists += game_data["Assists"]
                self.total_games += 1

                # Count wins and losses
                if game_data["Win/Loss"].strip().lower() == "win":
                    self.total_wins += 1
                    map_wins[game_data["Map"].strip()] += 1
                    mode_wins[game_data["Mode"].strip()] += 1
                    weapon_counter[game_data["Weapon"].strip()] += 1
                elif game_data["Win/Loss"].strip().lower() == "loss":
                    self.total_losses += 1

                # Count abilities, weapons, and modules usage
                ability_counter[game_data["Ability"].strip()] += 1
                weapon_counter[game_data["Weapon"].strip()] += 1
                module_counter[game_data["Module"].strip()] += 1

                # Track weapon K/D ratio (kills divided by deaths)
                kills = game_data["Kills"]
                deaths = max(1, game_data["Deaths"])  # Avoid division by zero
                weapon_kd_ratio[game_data["Weapon"]] = weapon_kd_ratio.get(game_data["Weapon"], 0) + (kills / deaths)

        # Calculate overall statistics
        self.kd_ratio = round(self.total_kills / max(1, self.total_deaths), 2)  # K/D ratio
        self.win_ratio = round((self.total_wins / max(1, self.total_games)) * 100, 2)  # Win/Loss ratio in percentage

        # Find the most used items based on counts
        self.most_used_ability = ability_counter.most_common(1)[0][0] if ability_counter else "None"
        self.most_used_weapon = weapon_counter.most_common(1)[0][0] if weapon_counter else "None"
        self.most_used_module = module_counter.most_common(1)[0][0] if module_counter else "None"
        
        # Find the best map, mode, and weapon based on wins and K/D ratio
        self.best_map = map_wins.most_common(1)[0][0] if map_wins else "None"
        self.best_mode = mode_wins.most_common(1)[0][0] if mode_wins else "None"
        self.best_weapon = max(weapon_kd_ratio, key=weapon_kd_ratio.get, default="None")

    # Helper function to update usage and win counts for stats
    def _update_stats(self, key, is_win, stats_dict):
        if key not in stats_dict:
            stats_dict[key] = {"wins": 0, "games": 0}  # Initialize if key doesn't exist
        stats_dict[key]["games"] += 1  # Increment total games count
        if is_win:
            stats_dict[key]["wins"] += 1  # Increment win count if it's a win

    # Helper function to get the best item by win rate
    def _get_best_by_win_rate(self, stats_dict):
        best_item = "None"
        best_win_rate = 0

        # Loop through each item to calculate win rate
        for key, stats in stats_dict.items():
            win_rate = stats["wins"] / stats["games"] if stats["games"] > 0 else 0
            if win_rate > best_win_rate:  # Find the highest win rate
                best_win_rate = win_rate
                best_item = key

        return best_item  # Return the item with the best win rate

    # Helper function to get the most used item
    def _get_most_used(self, stats_dict):
        return max(stats_dict, key=lambda k: stats_dict[k]["games"], default="None")

    def reset_fields(self):
            self.ui.spinBox_kills.setValue(0)
            self.ui.spinBox_deaths.setValue(0)
            self.ui.spinBox_assists.setValue(0)
            self.ui.comboBox_ability.setCurrentIndex(0)
            self.ui.comboBox_weapon.setCurrentIndex(0)
            self.ui.comboBox_module.setCurrentIndex(0)
            self.ui.comboBox_map.setCurrentIndex(0)
            self.ui.comboBox_win_loss.setCurrentIndex(0)
            self.ui.comboBox_mode.setCurrentIndex(0)
            self.ui.lineEdit_season.setText("None")
            
    def get_next_game_number(self, season_data, base_name):
        # Count existing games that start with the base name
        existing_games = [game for game in season_data.keys() if game.startswith(base_name)]
        
        # If there are no existing games, return 1
        if not existing_games:
            return 1
        
        # Extract the numeric part of the existing game names
        game_numbers = []
        for game in existing_games:
            # Extract the number from the game name (e.g., "Game1" -> 1)
            number_part = game[len(base_name):]  # Get the part after the base name
            if number_part.isdigit():
                game_numbers.append(int(number_part))
        
        # Return the next available game number
        return max(game_numbers) + 1 if game_numbers else 1

    # Function to save game data to a specific season and game file
    def save_game_data(self):
        # Check if the file exists and is not empty
        if BASE_DIR.exists() and BASE_DIR.stat().st_size > 0:
            # Load the existing data from the JSON file
            with open(BASE_DIR, "r") as jsonfile:
                data = json.load(jsonfile)
        else:
            # Initialize data as an empty dictionary if the file doesn't exist or is empty
            data = {}

        # Get the season from the lineEdit_season
        season = self.ui.lineEdit_season.text()

        # Ensure the season exists
        if season not in data:
            data[season] = {}

        # Prepare game data with a timestamp
        game_data = {
            "DateTime": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Kills": self.ui.spinBox_kills.value(),
            "Deaths": self.ui.spinBox_deaths.value(),
            "Assists": self.ui.spinBox_assists.value(),
            "Ability": self.ui.comboBox_ability.currentText(),
            "Weapon": self.ui.comboBox_weapon.currentText(),
            "Module": self.ui.comboBox_module.currentText(),
            "Mode": self.ui.comboBox_mode.currentText(),
            "Map": self.ui.comboBox_map.currentText(),
            "Win/Loss": self.ui.comboBox_win_loss.currentText(),
            "Timestamp": datetime.now().timestamp()  # Store the creation timestamp
        }

        # Add the game data to the season
        data[season][f"Game{len(data[season]) + 1}"] = game_data  # Temporary name

        # Save the updated data back to the JSON file
        with open(BASE_DIR, "w") as jsonfile:
            json.dump(data, jsonfile, indent=4)
    
    def rename_games(self, season):
        # Load the existing data from the JSON file
        with open(BASE_DIR, "r") as jsonfile:
            data = json.load(jsonfile)

        # Get the games for the specified season
        games = data[season]

        # Sort games by their timestamp in ascending order
        sorted_games = sorted(games.items(), key=lambda item: item[1]["Timestamp"])

        # Clear the current season's games before renaming
        data[season] = {}

        # Rename games based on their order
        for index, (game_name, game_data) in enumerate(sorted_games):
            new_game_name = f"Game{index + 1}"
            data[season][new_game_name] = game_data  # Assign the game data to the new name

        # Save the updated data back to the JSON file
        with open(BASE_DIR, "w") as jsonfile:
            json.dump(data, jsonfile, indent=4)

    def load_saved_games(self):
        # Clear existing widgets in the scroll area
        for i in reversed(range(self.ui.verticalLayout.count() - 1)):
            widget = self.ui.verticalLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        font5 = QFont()
        font5.setFamily("Moon")
        font5.setPointSize(12)

        # Load the game data from the JSON file
        with open(BASE_DIR, "r") as jsonfile:
            data = json.load(jsonfile)

        # Loop through each season in the JSON data
        for season, games in data.items():
            # Loop through each game in the season
            for game_name, game_data in games.items():
                # Create a new frame for each game
                frame = QFrame(self.ui.scrollAreaWidgetContents_2)
                sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
                frame.setSizePolicy(sizePolicy1)
                frame.setMinimumSize(0, 110)
                frame.setFrameShape(QFrame.Shape.StyledPanel)

                # Dynamically add labels for the game data
                label_game = QLabel(game_name[4:], frame)
                label_game.setGeometry(10, 10, 61, 21)
                label_game.setFont(font5)

                label_kills = QLabel(f"Kills: {game_data['Kills']}", frame)
                label_kills.setGeometry(10, 40, 200, 16)
                label_kills.setFont(font5)

                label_deaths = QLabel(f"Deaths: {game_data['Deaths']}", frame)
                label_deaths.setGeometry(10, 60, 200, 16)
                label_deaths.setFont(font5)

                label_assists = QLabel(f"Assists: {game_data['Assists']}", frame)
                label_assists.setGeometry(10, 80, 200, 16)
                label_assists.setFont(font5)

                label_ability = QLabel(f"Ability: {game_data['Ability']}", frame)
                label_ability.setGeometry(100, 40, 250, 16)
                label_ability.setFont(font5)

                label_weapon = QLabel(f"Weapon: {game_data['Weapon']}", frame)
                label_weapon.setGeometry(100, 60, 250, 16)
                label_weapon.setFont(font5)

                label_module = QLabel(f"Module: {game_data['Module']}", frame)
                label_module.setGeometry(100, 80, 250, 16)
                label_module.setFont(font5)

                label_mode = QLabel(f"Mode: {game_data['Mode']}", frame)
                label_mode.setGeometry(340, 40, 200, 16)
                label_mode.setFont(font5)

                label_map = QLabel(f"Map: {game_data['Map']}", frame)
                label_map.setGeometry(340, 60, 200, 16)
                label_map.setFont(font5)

                label_win_loss = QLabel(f"Win/Loss: {game_data['Win/Loss']}", frame)
                label_win_loss.setGeometry(340, 80, 200, 16)
                label_win_loss.setFont(font5)
                
                # Add K/D label
                kd_value = f"{int(game_data['Kills']) / max(1, int(game_data['Deaths'])):.2f}"  # Avoid division by zero
                label_kd = QLabel(f"K/D: {kd_value}", frame)
                label_kd.setGeometry(QRect(100, 10, 100, 21))
                label_kd.setFont(font5)
                
                # Add Date/Time label
                label_datetime = QLabel(f"Date/Time: {game_data['DateTime']}", frame)
                label_datetime.setGeometry(QRect(340, 10, 250, 21))
                label_datetime.setFont(font5)

                # Add Season label
                label_season = QLabel(f"Season: {season}", frame)
                label_season.setGeometry(QRect(630, 10, 150, 21))
                
                # Add buttons for editing and deleting the game
                btn_edit = QPushButton("Edit", frame)
                btn_edit.setFont(font5)
                btn_edit.setStyleSheet("color: rgb(0, 85, 255);")
                btn_edit.setGeometry(590, 70, 75, 24)  # Adjust position as needed

                btn_delete = QPushButton("Delete", frame)
                btn_delete.setFont(font5)
                btn_delete.setStyleSheet("color: rgb(255, 0, 0);")
                btn_delete.setGeometry(670, 70, 75, 24)  # Adjust position as needed
                
                # Find the index of the spacer
                spacer_index = self.ui.verticalLayout.indexOf(self.ui.verticalSpacer_2) 

                # Insert the frame before the spacer
                if spacer_index != -1:
                    self.ui.verticalLayout.insertWidget(spacer_index, frame)
                else:
                    self.ui.verticalLayout.addWidget(frame)  # Fallback if spacer not found
                    
                # Connect buttons to their actions (edit/delete game functions)
                btn_edit.clicked.connect(lambda _, g=game_name, s=season: self.edit_game(g, s))
                btn_delete.clicked.connect(lambda _, g=game_name, s=season: self.delete_game(g, s))
        
    def edit_game(self, game_name, season):
        # Load the game data from the JSON file
        with open(BASE_DIR, "r") as jsonfile:
            data = json.load(jsonfile)

        # Check if the game exists in the specified season
        if season not in data or game_name not in data[season]:
            return  # Exit the method if the game is not found

        # Get the specific game data
        game_data = data[season][game_name]

        # Populate the fields in the editor window with game data
        self.editor_window = GameDataEditor(game_name=game_name, season=season, main_window=self, load_saved_games=self.load_saved_games, get_next_game_number=self.get_next_game_number, rename_games=self.rename_games)
        self.editor_window.ui.label_41.setText(game_name)
        self.editor_window.ui.spinBox_kills.setValue(int(game_data['Kills']))
        self.editor_window.ui.spinBox_deaths.setValue(int(game_data['Deaths']))
        self.editor_window.ui.spinBox_assists.setValue(int(game_data['Assists']))
        self.editor_window.ui.comboBox_ability.setCurrentText(game_data['Ability'])
        self.editor_window.ui.comboBox_weapon.setCurrentText(game_data['Weapon'])
        self.editor_window.ui.comboBox_module.setCurrentText(game_data['Module'])
        self.editor_window.ui.comboBox_mode.setCurrentText(game_data['Mode'])
        self.editor_window.ui.comboBox_map.setCurrentText(game_data['Map'])
        self.editor_window.ui.comboBox_win_loss.setCurrentText(game_data['Win/Loss'])
        self.editor_window.ui.date_lineEdit.setText(game_data['DateTime'])

        # Calculate K/D ratio and display it
        kd_value = f"{int(game_data['Kills']) / max(1, int(game_data['Deaths'])):.2f}"
        self.editor_window.ui.label_42.setText("K/D: " + kd_value)

        # Set the season in the editor window
        self.editor_window.ui.lineEdit_season.setText(season)

        # Show the editor window
        self.editor_window.show()

    # Function to delete a specific game file
    def delete_game(self, game_name, season):
        # Load the game data from the JSON file
        with open(BASE_DIR, "r") as jsonfile:
            data = json.load(jsonfile)

        # Remove the specific game from the JSON data
        if season in data and game_name in data[season]:
            del data[season][game_name]

            # Save the updated data back to the JSON file
            with open(BASE_DIR, "w") as jsonfile:
                json.dump(data, jsonfile, indent=4)

            self.load_saved_games()  # Reload the history tab to update the view

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    icon = QIcon("assets/app.ico")
    app.setWindowIcon(icon)
    app_id = str(uuid.uuid4())
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    window.show()
    sys.exit(app.exec())