# 事前準備
- Pipenvのインストール (Macの場合、`brew install pipenv`など)
- Blenderのインストール （新しめのものを推奨。作者は 2.93.2 で動作確認）
    - blenderコマンドにパスを通す必要あり
- Makeコマンドのインストール（Mac/Linux ではデフォルトで動作するはず）

# プロジェクトのセットアップ
- make init

# 使い方

`ANGLE_STEP=90 CAM_DISTANCE=10 FILE=./assets/default.fbx make run`

## パラメータ

| パラメータ   | 意味                                               | デフォルト値         | 
| ------------ | -------------------------------------------------- | -------------------- | 
| ANGLE_STEP   | レンダリング時にカメラを回転させる角度の間隔（度） | 90                   | 
| CAM_DISTANCE | レンダリング時の原点からのカメラの距離（ｍ）       | 10                   | 
| FILE         | レンダリングするファイルパス                       | ./assets/default.fbx | 


# その他コマンド
- make test ... ユニットテストを実行
- make reset ... 作成した画像やBlenderファイルを削除