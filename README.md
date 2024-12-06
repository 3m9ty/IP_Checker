<!-- 底下標籤來源參考寫法可至：https://github.com/Envoy-VC/awesome-badges#github-stats -->


# IP Checker

IP檢查並結合Discord Bot通知功能
若架設簡易伺服器為浮動IP，可透過此工具於IP變更時，自動將IP更新於指定Discord頻道


## 功能

1. 於設定時間內執行IP檢查 (預設為1200 sec，未來將參數化)
2. 於綁定的伺服器任意頻道內，輸入指令即可主動檢查IP
```bash
!ip
```

## 安裝與使用

以下將會引導你如何安裝此專案到你的電腦上。

Python 版本建議為：`3.12.x` 以上...

### 取得專案

```bash
git clone git@github.com:hsiangfeng/README-Example-Template.git
```

### 移動到專案內

```bash
cd README-Example-Template
```

### 安裝套件

```bash
pip install requests
pip install discord
pip install asyncio
```

### 運行專案

```bash
python ip_checker.py
```

## 版本紀錄

- 1.0: 正式將工具上線
- 1.1: 增加時間標記以及偵測通知，包括於 Discord 和 Terminal  
- Future: 將Server Token、Channel ID 和 檢查時間 參數化
- Future: 增加更多相關指令，增進使用體驗


## 聯絡作者

作者 : Empty_Oreo

可以透過以下方式與我聯絡
- E-mail: ylwei6627@gmail.com

