import sys
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

FOLDER_DIR = Path("data")
JSON_FILE = FOLDER_DIR / "game_data.json"

if not FOLDER_DIR.exists():
    FOLDER_DIR.mkdir(parents=True)
    
if not JSON_FILE.exists():
    with open(JSON_FILE, "w") as jsonfile:
        json.dump({"Y1S1":{}}, jsonfile)

# Location of your data
BASE_DIR = JSON_FILE

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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 50, 801, 551))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 750, 61))
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
        self.comboBox_weapon.setGeometry(QRect(340, 120, 171, 31))
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
        self.comboBox_module.setGeometry(QRect(340, 150, 171, 31))
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
        self.comboBox_ability.setGeometry(QRect(340, 90, 171, 31))
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
        self.scrollArea_2.setGeometry(QRect(0, 0, 791, 521))
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
        self.progressBar_win_ratio_general.setGeometry(QRect(480, 20, 261, 31))
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
        self.most_used_ability_lable_general.setGeometry(QRect(10, 200, 400, 31))
        self.most_used_ability_lable_general.setFont(font3)
        self.most_used_weapon_lable_general = QLabel(self.general_statistics)
        self.most_used_weapon_lable_general.setObjectName(u"most_used_weapon_lable_general")
        self.most_used_weapon_lable_general.setGeometry(QRect(10, 230, 400, 31))
        self.most_used_weapon_lable_general.setFont(font3)
        self.most_used_module_lable_general = QLabel(self.general_statistics)
        self.most_used_module_lable_general.setObjectName(u"most_used_module_lable_general")
        self.most_used_module_lable_general.setGeometry(QRect(10, 260, 400, 31))
        self.most_used_module_lable_general.setFont(font3)
        self.best_map_lable_general = QLabel(self.general_statistics)
        self.best_map_lable_general.setObjectName(u"best_map_lable_general")
        self.best_map_lable_general.setGeometry(QRect(430, 260, 300, 31))
        self.best_map_lable_general.setFont(font3)
        self.best_weapon_lable_general = QLabel(self.general_statistics)
        self.best_weapon_lable_general.setObjectName(u"best_weapon_lable_general")
        self.best_weapon_lable_general.setGeometry(QRect(430, 230, 300, 31))
        self.best_weapon_lable_general.setFont(font3)
        self.best_mode_lable_general = QLabel(self.general_statistics)
        self.best_mode_lable_general.setObjectName(u"best_mode_lable_general")
        self.best_mode_lable_general.setGeometry(QRect(430, 200, 300, 31))
        self.best_mode_lable_general.setFont(font3)

        self.verticalLayout_2.addWidget(self.general_statistics)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.scrollArea = QScrollArea(self.tab_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(8, 7, 781, 511))
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BattleCore Tracker", None))
        self.actiong.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BattleCore Tracker - V.1", None))
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

        self.comboBox_ability.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_ability.setItemText(1, QCoreApplication.translate("MainWindow", u"Blast", None))
        self.comboBox_ability.setItemText(2, QCoreApplication.translate("MainWindow", u"Shield Healing", None))
        self.comboBox_ability.setItemText(3, QCoreApplication.translate("MainWindow", u"Teleportation", None))
        self.comboBox_ability.setItemText(4, QCoreApplication.translate("MainWindow", u"Invisibility", None))
        self.comboBox_ability.setItemText(5, QCoreApplication.translate("MainWindow", u"Flash Bang", None))
        self.comboBox_ability.setItemText(6, QCoreApplication.translate("MainWindow", u"Black Hole", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Map:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Win/Loss:", None))
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

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.comboBox_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Backup", None))
        self.comboBox_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Q-Ball", None))
        self.comboBox_mode.setItemText(3, QCoreApplication.translate("MainWindow", u"Free for All", None))
        self.comboBox_mode.setItemText(4, QCoreApplication.translate("MainWindow", u"Ranked", None))
        self.comboBox_mode.setItemText(5, QCoreApplication.translate("MainWindow", u"Co-op vs. AIs", None))
        self.comboBox_mode.setItemText(6, QCoreApplication.translate("MainWindow", u"Custom", None))

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
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"BattleCore Tracker", None))
    # retranslateUi

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

# Define the MainWindow class
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the tab change signal to the method
        self.ui.tabWidget.currentChanged.connect(self.on_tab_change)
        # Connect the button click event to the save_game_data method
        self.ui.pushButton_save_game.clicked.connect(self.save_game_data)
        # Connect the button click event to the reset_fields method
        self.ui.pushButton_reset.clicked.connect(self.reset_fields)
        
    def on_tab_change(self, index):
        
        if index == 3:
            # Call load_saved_games only if the game_data.json file exists
            if BASE_DIR.exists():
                self.load_saved_games()
        
        if index == 2:
            # Call load_general_stats only if the game_data.json file exists
            if BASE_DIR.exists():
                self.load_general_stats()

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
        self.ui.most_used_ability_lable_general.setText(f"Most Used Ability: {self.most_used_ability}")
        self.ui.most_used_weapon_lable_general.setText(f"Most Used Weapon: {self.most_used_weapon}")
        self.ui.most_used_module_lable_general.setText(f"Most Used Module: {self.most_used_module}")
        self.ui.best_map_lable_general.setText(f"Best Map: {self.best_map}")
        self.ui.best_mode_lable_general.setText(f"Best Mode: {self.best_mode}")
        self.ui.best_weapon_lable_general.setText(f"Best Weapon: {self.best_weapon}")

        # Clear previous seasonal stats if any, but keep the general stats
        for i in reversed(range(self.ui.verticalLayout_2.count())): 
            widget = self.ui.verticalLayout_2.itemAt(i).widget()
            if widget is not None and widget.objectName() != "general_statistics":  # Adjust this check as needed
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
            if game_data["Win/Loss"].lower() == "win":
                total_wins += 1
                map_wins[game_data["Map"]] += 1
                mode_wins[game_data["Mode"]] += 1
            elif game_data["Win/Loss"].lower() == "loss":
                total_losses += 1

            # Count abilities, weapons, and modules usage
            ability_counter[game_data["Ability"]] += 1
            weapon_counter[game_data["Weapon"]] += 1
            module_counter[game_data["Module"]] += 1

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

        progressBar_win_ratio = QProgressBar(season_group_box)
        progressBar_win_ratio.setGeometry(QRect(480, 20, 261, 31))
        progressBar_win_ratio.setValue(win_ratio)
        progressBar_win_ratio.setTextVisible(False)

        kills_label = QLabel(f"Kills: {total_kills}", season_group_box)
        kills_label.setGeometry(QRect(10, 50, 200, 31))

        deaths_label = QLabel(f"Deaths: {total_deaths}", season_group_box)
        deaths_label.setGeometry(QRect(10, 80, 200, 31))

        assists_label = QLabel(f"Assists: {total_assists}", season_group_box)
        assists_label.setGeometry(QRect(10, 110, 200, 31))

        wins_label = QLabel(f"Wins: {total_wins}", season_group_box)
        wins_label.setGeometry(QRect(240, 50, 200, 31))

        losses_label = QLabel(f"Losses: {total_losses}", season_group_box)
        losses_label.setGeometry(QRect(240, 80, 200, 31))

        matches_label = QLabel(f"Matches: {total_games}", season_group_box)
        matches_label.setGeometry(QRect(240, 110, 200, 31))

        # Add most used ability, weapon, and module
        most_used_ability_label = QLabel(f"Most Used Ability: {most_used_ability}", season_group_box)
        most_used_ability_label.setGeometry(QRect(10, 200, 400, 31))

        most_used_weapon_label = QLabel(f"Most Used Weapon: {most_used_weapon}", season_group_box)
        most_used_weapon_label.setGeometry(QRect(10, 230, 400, 31))

        most_used_module_label = QLabel(f"Most Used Module: {most_used_module}", season_group_box)
        most_used_module_label.setGeometry(QRect(10, 260, 400, 31))

        # Add best map, mode, and weapon labels
        best_map_label = QLabel(f"Best Map: {best_map}", season_group_box)
        best_map_label.setGeometry(QRect(430, 260, 300, 31))

        best_mode_label = QLabel(f"Best Mode: {best_mode}", season_group_box)
        best_mode_label.setGeometry(QRect(430, 200, 300, 31))

        best_weapon_label = QLabel(f"Best Weapon: {best_weapon}", season_group_box)
        best_weapon_label.setGeometry(QRect(430, 230, 300, 31))

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
                if game_data["Win/Loss"].lower() == "win":
                    self.total_wins += 1
                    map_wins[game_data["Map"]] += 1
                    mode_wins[game_data["Mode"]] += 1
                    weapon_counter[game_data["Weapon"]] += 1
                elif game_data["Win/Loss"].lower() == "loss":
                    self.total_losses += 1

                # Count abilities, weapons, and modules usage
                ability_counter[game_data["Ability"]] += 1
                weapon_counter[game_data["Weapon"]] += 1
                module_counter[game_data["Module"]] += 1

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
                label_game = QLabel(f"{game_name}", frame)
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

            # Reload the saved games
            self.load_saved_games()  # Reload the history tab to update the view

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())