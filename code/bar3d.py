# 3D棒グラフの作成

# 利用するライブラリ
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#%%

### 値の指定

## スカラの場合

# 起点を指定
x = 0.0
y = 0.0
z = 0.0

# バーのハーフサイズの値を指定
a = 0.5

# 変化量を指定
dx = a * 2.0
dy = a * 2.0
dz = 1.0

#%%

## 1次元配列の場合

# 値を作成
vals = np.arange(3)

# 格子点を作成
X, Y = np.meshgrid(vals, vals)

# 起点を設定
x = X.flatten()
y = Y.flatten()
z = np.zeros_like(x)

# バーのハーフサイズの値を指定
a = 0.5

# 変化量を指定
dx = np.repeat(a=a * 2.0, repeats=len(x))
dy = np.repeat(a=a * 2.0, repeats=len(y))
dz = np.arange(len(z))

#%%

### 引数とバーの関係

# 3D棒グラフを作成
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x, y=y, z=z, dx=dx, dy=dy, dz=dz, color='white', alpha=0.25) # 3D棒グラフ
ax.scatter(xs=x, ys=y, zs=z, s=100, color='purple', label='(x, y, z)') # 起点
ax.scatter(xs=x+dx, ys=y, zs=z, s=100, color='red', label='(x+dx, y, z)') # x軸方向に変化した点
ax.scatter(xs=x, ys=y+dy, zs=z, s=100, color='pink', label='(x, y+dy, z)') # y軸方向に変化した点
ax.scatter(xs=x, ys=y, zs=z+dz, s=100, color='orange', label='(x, y, z+dz)') # z軸方向に変化した点
ax.scatter(xs=x+dx, ys=y+dy, zs=z+dz, s=100, color='springgreen', label='(x+dx, y+dy, z+dz)') # 全ての軸で変化した点
ax.quiver(x, y, z, dx, 0.0, 0.0, color='purple', linestyle='--', arrow_length_ratio=0.1) # x軸の変化量
ax.quiver(x, y, z, 0.0, dy, 0.0, color='purple', linestyle='--', arrow_length_ratio=0.1) # y軸の変化量
ax.quiver(x, y, z, 0.0, 0.0, dz, color='purple', linestyle='--', arrow_length_ratio=0.1) # z軸の変化量
ax.quiver(x, y, z, dx, dy, dz, color='purple', arrow_length_ratio=0.1) # 全ての軸の変化量
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('bar3d', fontsize='20') # タイトル
fig.legend() # 凡例
#ax.view_init(elev=90, azim=270) # 表示アングル
plt.show() # 描画

# 3D棒グラフを作成
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x, y=y, z=z, dx=dx, dy=dy, dz=dz, color='white', alpha=0.25) # 3D棒グラフ
ax.scatter(xs=x, ys=y, zs=z, s=100, color='purple', label='(x, y, z)') # 起点
ax.scatter(xs=x+dx, ys=y, zs=z, s=100, color='red', label='(x+dx, y, z)') # x軸方向に変化した点
ax.scatter(xs=x+dx, ys=y+dy, zs=z, s=100, color='aqua', label='(x+dx, y+dy, z)') # x軸とy軸方向に変化した点
ax.scatter(xs=x+dx, ys=y+dy, zs=z+dz, s=100, color='springgreen', label='(x+dx, y+dy, z+dz)') # 全ての軸で変化した点
ax.quiver(x, y, z, dx, 0.0, 0.0, color='purple', linestyle=':', arrow_length_ratio=0.1) # x軸の変化量
ax.quiver(x+dx, y, z, 0.0, dy, 0.0, color='purple', linestyle=':', arrow_length_ratio=0.1) # y軸の変化量
ax.quiver(x+dx, y+dy, z, 0.0, 0.0, dz, color='purple', linestyle=':', arrow_length_ratio=0.1) # z軸の変化量
ax.quiver(x, y, z, dx, dy, dz, color='purple', arrow_length_ratio=0.1) # 全ての軸の変化量
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('bar3d', fontsize='20') # タイトル
fig.legend() # 凡例
#ax.view_init(elev=90, azim=270) # 表示アングル
plt.show() # 描画

#%%

### 起点の調整

# デフォルトの設定
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x, y=y, z=z, dx=dx, dy=dy, dz=dz, color='white', alpha=0.5) # 3D棒グラフ
ax.scatter(xs=x, ys=y, zs=z, s=100, color='purple', label='(x, y, z)') # 起点
ax.quiver(x, y, z, dx, 0.0, 0.0, color='purple', linestyle='--', arrow_length_ratio=0.1) # x軸の変化量
ax.quiver(x, y, z, 0.0, dy, 0.0, color='purple', linestyle='--', arrow_length_ratio=0.1) # y軸の変化量
ax.quiver(x, y, z, 0.0, 0.0, dz, color='purple', linestyle='--', arrow_length_ratio=0.1) # z軸の変化量
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('(x, y, z)', fontsize='20') # タイトル
fig.legend() # 凡例
#ax.view_init(elev=90, azim=270) # 表示アングル
plt.show() # 描画

# 起点をズラす
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, color='white', alpha=0.5) # 3D棒グラフ
ax.scatter(xs=x, ys=y, zs=z, color='purple', s=100, label='(x, y, z)') # 元の起点
ax.scatter(xs=x-a, ys=y-a, zs=z, color='green', s=100, label='(x-' + str(a) + ', y-' + str(a) + ', z)') # 調整後の起点
ax.quiver(x-a, y-a, z, dx, 0.0, 0.0, color='green', linestyle='--', arrow_length_ratio=0.1) # x軸の変化量
ax.quiver(x-a, y-a, z, 0.0, dy, 0.0, color='green', linestyle='--', arrow_length_ratio=0.1) # y軸の変化量
ax.quiver(x-a, y-a, z, 0.0, 0.0, dz, color='green', linestyle='--', arrow_length_ratio=0.1) # z軸の変化量
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('(x-a, y-a, z)', fontsize='20') # タイトル
fig.legend() # 凡例
#ax.view_init(elev=90, azim=270) # 表示アングル
plt.show() # 描画

#%%

### shade引数

# 影を付ける:(デフォルト)
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x, y=y, z=z, dx=dx, dy=dy, dz=dz, shade=True) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('shade=True', fontsize='20') # タイトル
#ax.view_init(elev=90, azim=270) # 表示アングル
plt.show() # 描画

# 影を消す
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, shade=False) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('shade=False', fontsize='20') # タイトル
#ax.view_init(elev=90, azim=270) # 表示アングル
plt.show() # 描画

#%%

### color引数

# カラーマップを指定
cm = plt.get_cmap('jet')

# RGBA情報に変換
print(cm(1.0))

# カラーマップを指定
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, 
         color=cm(dz / np.max(dz)), alpha=0.5) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title("cmap='jet'", fontsize='20') # タイトル
plt.show() # 描画

#%%

### edgecolor引数

# カラーマップを指定
cm = plt.get_cmap('rainbow')

# デフォルトの設定
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, 
         color=cm(dz / np.max(dz)), edgecolor=cm(dz / np.max(dz)), alpha=0.5) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('edgecolor=cm(...)', fontsize='20') # タイトル
plt.show() # 描画

# 面と辺の色を一致させる
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, 
         color=cm(dz / np.max(dz)), edgecolor=cm(np.repeat(dz / np.max(dz), 6)), alpha=0.5) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('edgecolor=cm(np.repeat(..., 6))', fontsize='20') # タイトル
plt.show() # 描画

#%%

# カラーマップを指定
cm = plt.get_cmap('rainbow')

# カラーマップを確認
plt.figure(figsize=(9, 8)) # 図の設定
plt.scatter(np.arange(6), np.arange(6), color=cm(np.arange(6) / 5), s=250) # 散布図
plt.grid() # グリッド線
plt.title("cmap='rainbow'", fontsize=20) # タイトル
plt.show() # 描画

# 辺の色付け順を確認
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=-0.5, y=-0.5, z=0.0, dx=1.0, dy=1.0, dz=1.0, 
         color='white', edgecolors=cm(np.arange(6) / 5), linewidth=5, alpha=0.5) # 3D棒グラフ
ax.text(x=0.0, y=0.0, z=0.0, s='-Z', color=cm(0 / 5), fontsize=20) # -Zの面
ax.text(x=0.0, y=0.0, z=1.0, s='+Z', color=cm(1 / 5), fontsize=20) # +Zの面
ax.text(x=0.0, y=-0.5, z=0.5, s='-Y', color=cm(2 / 5), fontsize=20) # -Yの面
ax.text(x=0.0, y=0.5, z=0.5, s='+Y', color=cm(3 / 5), fontsize=20) # +Yの面
ax.text(x=-0.5, y=0.0, z=0.5, s='-X', color=cm(4 / 5), fontsize=20) # -Xの面
ax.text(x=0.5, y=0.0, z=0.5, s='+X', color=cm(5 / 5), fontsize=20) # +Xの面
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('edgecolors=[-Z, +Z, -Y, +Y, -X, +X]', fontsize='20') # タイトル
#ax.view_init(elev=0, azim=270) # 表示アングル
plt.show() # 描画

#%%

# 作図用の角度を作成
v_vals = np.arange(start=-90.0, stop=270.0, step=3.0)
h_vals = np.arange(start=0.0, stop=360.0, step=3.0)

# カラーマップを指定
cm = plt.get_cmap('rainbow')

# 図を初期化
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(projection='3d') # 3D用の設定

# 作図処理を関数として定義
def update(i):
    # 前フレームのグラフを初期化
    plt.cla()
    
    # i回目の角度を取得
    #v = 0.0
    h = 180.0
    v = v_vals[i]
    #h = h_vals[i]
    
    # 3D棒グラフを作成
    ax.bar3d(x=-0.5, y=-0.5, z=0.0, dx=1.0, dy=1.0, dz=1.0, 
             color='white', edgecolors=cm(np.arange(6) / 5), linewidth=5, alpha=0.5) # 3D棒グラフ
    ax.text(x=0.0, y=0.0, z=0.0, s='-Z', color=cm(0 / 5), fontsize=20) # -Zの面
    ax.text(x=0.0, y=0.0, z=1.0, s='+Z', color=cm(1 / 5), fontsize=20) # +Zの面
    ax.text(x=0.0, y=-0.5, z=0.5, s='-Y', color=cm(2 / 5), fontsize=20) # -Yの面
    ax.text(x=0.0, y=0.5, z=0.5, s='+Y', color=cm(3 / 5), fontsize=20) # +Yの面
    ax.text(x=-0.5, y=0.0, z=0.5, s='-X', color=cm(4 / 5), fontsize=20) # -Xの面
    ax.text(x=0.5, y=0.0, z=0.5, s='+X', color=cm(5 / 5), fontsize=20) # +Xの面
    ax.set_xlabel('x') # x軸ラベル
    ax.set_ylabel('y') # y軸ラベル
    ax.set_zlabel('z') # z軸ラベル
    if v < 0: # (270 < v < 360の範囲で軸が反転する対策)
        ax.set_title('v=' + str(np.round(360.0 + v)) + ', h=' + str(np.round(h))) # タイトル
    elif v >= 0:
        ax.set_title('v=' + str(np.round(v)) + ', h=' + str(np.round(h))) # タイトル
    ax.view_init(elev=v, azim=h) # 表示アングル

# gif画像を作成
anime_bar3d = FuncAnimation(fig, update, frames=len(v_vals), interval=100)

# gif画像を保存
anime_bar3d.save('Matplotlib/figure/bar3d_v.gif')

#%%

###　軸目盛の設定

# 軸目盛の表示位置を指定
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, 
         color=cm(dz / np.max(dz)), alpha=0.5) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('ticks', fontsize='20') # タイトル
ax.set_xticks(ticks=vals) # x軸目盛
ax.set_yticks(ticks=vals) # y軸目盛
plt.show() # 描画

# 軸目盛の表示位置と文字列を指定
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, 
         color=cm(dz / np.max(dz)), alpha=0.5) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('ticks, ticklabels', fontsize='20') # タイトル
ax.set_xticks(ticks=vals) # x軸目盛
ax.set_yticks(ticks=vals) # y軸目盛
ax.set_xticklabels(labels=['$x_' + str(int(i)) + '$' for i in vals]) # x軸目盛ラベル
ax.set_yticklabels(labels=['$y_' + str(int(i)) + '$' for i in vals]) # y軸目盛ラベル
plt.show() # 描画

#%%

# 起点を変更せずに目盛によって調整する
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x, y=y, z=z, dx=a*2.0, dy=a*2.0, dz=dz, 
         color=cm(dz / np.max(dz)), alpha=0.5) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('ticks, ticklabels', fontsize='20') # タイトル
ax.set_xticks(ticks=vals + a) # x軸目盛
ax.set_yticks(ticks=vals + a) # y軸目盛
ax.set_xticklabels(labels=vals) # x軸目盛ラベル
ax.set_yticklabels(labels=vals) # y軸目盛ラベル
plt.show() # 描画

# 調整の結果を確認
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.bar3d(x=x, y=y, z=z, dx=a*2.0, dy=a*2.0, dz=dz, color='white', alpha=0.5) # 3D棒グラフ
ax.quiver(x, y, z, dx, 0.0, 0.0, color='purple', linestyle='--', arrow_length_ratio=0.1) # x軸
ax.quiver(x, y, z, 0.0, dy, 0.0, color='purple', linestyle='--', arrow_length_ratio=0.1) # y軸
ax.quiver(x, y, z, 0.0, 0.0, dz, color='purple', linestyle='--', arrow_length_ratio=0.1) # z軸
ax.scatter(xs=x, ys=y, zs=z, s=100, color='purple', label='(x, y, z)') # 元の起点
ax.scatter(xs=x-a, ys=y-a, zs=z, color='green', s=100, label='(x-' + str(a) + ', y-' + str(a) + ', z)') # 実際に調整したときの起点
ax.scatter(xs=x+a, ys=y+a, zs=z, color='mediumblue', s=100, label='(x+' + str(a) + ', y+' + str(a) + ', z)') # 見掛け上の調整後の中心
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title('ticks, ticklabels', fontsize='20') # タイトル
ax.set_xticks(ticks=vals + a) # x軸目盛
ax.set_yticks(ticks=vals + a) # y軸目盛
ax.set_xticklabels(labels=vals) # x軸目盛ラベル
ax.set_yticklabels(labels=vals) # y軸目盛ラベル
fig.legend() # 凡例
#ax.view_init(elev=90, azim=270) # 表示アングル
plt.show() # 描画

#%%

### カラーバーの表示

# カラーマップを指定
cm = plt.get_cmap('jet')

# 3D棒グラフの作成
fig = plt.figure(figsize=(9, 8)) # 図の設定
ax = fig.add_subplot(projection='3d') # 3D用の設定
bar = ax.bar3d(x=x-a, y=y-a, z=z, dx=dx, dy=dy, dz=dz, 
         color=cm(dz / np.max(dz)), edgecolor=cm(np.repeat(dz / np.max(dz), 6)), alpha=0.5) # 3D棒グラフ
ax.set_xlabel('x') # x軸ラベル
ax.set_ylabel('y') # y軸ラベル
ax.set_zlabel('z') # z軸ラベル
ax.set_title("cmap='jet'", fontsize='20') # タイトル
mappable = plt.cm.ScalarMappable(cmap='jet') # Mappableオブジェクト
mappable.set_array(dz) # Mappableに値を設定
cbar = plt.colorbar(mappable, shrink=0.75, aspect=10) # カラーバー
cbar.set_label('z') # カラーバーラベル
#ax.view_init(elev=0, azim=300) # 表示アングル
plt.show() # 描画

#%%

