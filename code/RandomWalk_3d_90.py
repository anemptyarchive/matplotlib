
# 3次元(3方向)ランダムウォークの作図

# %%

# 利用するライブラリ
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# %%

### 乱数の生成

# 試行回数を指定
max_iter = 600

# サンプルサイズを指定
sample_size = 5

# 乱数を生成
random_val_arr  = np.random.choice([-1, 1], size=(sample_size, max_iter), replace=True) # 移動量
random_axis_arr = np.random.choice(['x', 'y', 'z'], size=(sample_size, max_iter), replace=True) # 移動軸

# 座標を計算
x_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.int32(random_axis_arr=='x') * random_val_arr]), # 初期値を追加
    axis=1
)
y_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.int32(random_axis_arr=='y') * random_val_arr]), # 初期値を追加
    axis=1
)
z_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.int32(random_axis_arr=='z') * random_val_arr]), # 初期値を追加
    axis=1
)

# %%

### グラフの作成：(座標軸のみ)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.max([np.abs(x_arr), np.abs(y_arr), np.abs(z_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")
color_num = 10 # カラーマップごとに固定

# 3Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(12, 12), facecolor='white', 
                       subplot_kw={'projection': '3d'})
for s in range(sample_size):
    
    # 最終値を取得
    x = x_arr[s, max_iter]
    y = y_arr[s, max_iter]
    z = z_arr[s, max_iter]

    ax.plot(x_arr[s], y_arr[s], zs=-axis_size, zdir='z', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
    ax.plot(y_arr[s], z_arr[s], zs=-axis_size, zdir='x', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # yz面の軌跡
    ax.plot(x_arr[s], z_arr[s], zs=axis_size, zdir='y', 
            color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xz面の軌跡
    ax.scatter([x, -axis_size, x], 
               [y, y, axis_size], 
               [-axis_size, z, z], 
               s=100, fc='none', ec=cmap(s%color_num)) # 面ごとの最終地点
    ax.quiver(x, y, z, 
              [0, -axis_size-x, 0], [0, 0, axis_size-y], [-axis_size-z, 0, 0], 
              arrow_length_ratio=0, color=cmap(s%color_num), linewidth=1, linestyle='dotted') # 点の目盛線
    ax.plot(x_arr[s], y_arr[s], z_arr[s], 
            color=cmap(s%color_num), alpha=0.4) # 軌跡
    ax.scatter(x, y, z, s=100, color=cmap(s%color_num)) # 最終地点
ax.margins(x=0.0, y=0.0, z=0.0) # (機能しない?のでlimで謎小細工)
ax.set_xlim(xmin=-axis_size/1.05, xmax=axis_size/1.05)
ax.set_ylim(ymin=-axis_size/1.05, ymax=axis_size/1.05)
ax.set_zlim(zmin=-axis_size/1.05, zmax=axis_size/1.05)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_box_aspect((1, 1, 1))

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/3d_90_xyz_n.png', dpi=250)

plt.show()

# %%

### アニメーションの作成：(座標軸のみ)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.max([np.abs(x_arr), np.abs(y_arr), np.abs(z_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(12, 12), facecolor='white', 
                       subplot_kw={'projection': '3d'})
fig.suptitle('Random Walk', fontsize=20)

# 矢サイズを指定
alr = 1

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")
color_num = 10 # カラーマップごとに固定

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()
    
    for s in range(sample_size):
        
        # 現在値を取得
        x = x_arr[s, i]
        y = y_arr[s, i]
        z = z_arr[s, i]
        
        ax.plot(x_arr[s, :i+1], y_arr[s, :i+1], zs=-axis_size, zdir='z', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
        ax.plot(y_arr[s, :i+1], z_arr[s, :i+1], zs=-axis_size, zdir='x', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # yz面の軌跡
        ax.plot(x_arr[s, :i+1], z_arr[s, :i+1], zs=axis_size, zdir='y', 
                color=cmap(s%color_num), alpha=0.4, linewidth=1, linestyle='dashed') # xz面の軌跡
        ax.scatter([x, -axis_size, x], 
                   [y, y, axis_size], 
                   [-axis_size, z, z], 
                   s=100, fc='none', ec=cmap(s%color_num)) # 面ごとの現在地点
        ax.quiver(x, y, z, 
                  [0, -axis_size-x, 0], [0, 0, axis_size-y], [-axis_size-z, 0, 0], 
                  arrow_length_ratio=0, color=cmap(s%color_num), linewidth=1, linestyle='dotted') # 点の目盛線
        ax.plot(x_arr[s, :i+1], y_arr[s, :i+1], z_arr[s, :i+1], 
                color=cmap(s%color_num), alpha=0.4) # 軌跡
        ax.scatter(x, y, z, s=100, color=cmap(s%color_num)) # 現在地点
    ax.margins(x=0.0, y=0.0, z=0.0) # (機能しない?のでlimで謎小細工)
    ax.set_xlim(xmin=-axis_size/1.05, xmax=axis_size/1.05)
    ax.set_ylim(ymin=-axis_size/1.05, ymax=axis_size/1.05)
    ax.set_zlim(zmin=-axis_size/1.05, zmax=axis_size/1.05)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('iteration: '+str(i), loc='left')
    ax.set_box_aspect((1, 1, 1))
    #ax.view_init(elev=30, azim=i) # 表示アングル

# 動画を作成
ani = FuncAnimation(fig=fig, func=update, frames=max_iter+1, interval=100)

# 動画を書出
ani.save(
    filename='../figure/RandomWalk/3d_90_xyz_n.mp4', dpi=250, 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)

# %%


