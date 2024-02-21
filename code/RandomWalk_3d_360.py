
# 3次元(全方向)ランダムウォークの作図

# %%

# 利用するライブラリ
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# %%

# 試行回数を指定
max_iter = 300

# サンプルサイズを指定
sample_size = 5

# 乱数を生成
random_t_arr = np.random.uniform(low=0, high=2*np.pi, size=(sample_size, max_iter)) # ラジアン
random_u_arr = np.random.uniform(low=0, high=2*np.pi, size=(sample_size, max_iter)) # ラジアン

# 試行ごとに集計
x_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.sin(random_t_arr)*np.cos(random_u_arr)]), # 初期値を追加
    axis=1
)
y_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.sin(random_t_arr)*np.sin(random_u_arr)]), # 初期値を追加
    axis=1
)
z_arr = np.cumsum(
    np.hstack([np.zeros((sample_size, 1)), np.cos(random_t_arr)]), # 初期値を追加
    axis=1
)

# %%

### グラフの作成：(座標軸のみ)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.max([np.abs(x_arr), np.abs(y_arr), np.abs(z_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# 矢サイズを指定
alr = 0.5

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")

# 3Dランダムウォークを作図
fig, ax = plt.subplots(figsize=(10, 10), dpi=250, facecolor='white', 
                       subplot_kw={'projection': '3d'})
for s in range(sample_size):
    
    # 最終値を取得
    x = x_arr[s, max_iter]
    y = y_arr[s, max_iter]
    z = z_arr[s, max_iter]

    ax.plot(x_arr[s], y_arr[s], zs=-axis_size, zdir='z', 
            color=cmap(s), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
    ax.plot(y_arr[s], z_arr[s], zs=-axis_size, zdir='x', 
            color=cmap(s), alpha=0.4, linewidth=1, linestyle='dashed') # yz面の軌跡
    ax.plot(x_arr[s], z_arr[s], zs=axis_size, zdir='y', 
            color=cmap(s), alpha=0.4, linewidth=1, linestyle='dashed') # xz面の軌跡
    ax.scatter([x, -axis_size, x], 
               [y, y, axis_size], 
               [-axis_size, z, z], 
               s=50, fc='none', ec=cmap(s)) # 面ごとの最終地点
    ax.quiver(x, y, z, 
              [0, -axis_size-x, 0], [0, 0, axis_size-y], [-axis_size-z, 0, 0], 
              arrow_length_ratio=0, color=cmap(s), linewidth=1, linestyle='dotted') # 点の目盛線
    ax.plot(x_arr[s], y_arr[s], z_arr[s], 
            color=cmap(s), alpha=0.5) # 軌跡
    ax.scatter(x, y, z, s=50, color=cmap(s)) # 最終地点
ax.set_xlim(xmin=-axis_size, xmax=axis_size)
ax.set_ylim(ymin=-axis_size, ymax=axis_size)
ax.set_zlim(zmin=-axis_size, zmax=axis_size)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('iteration: '+str(max_iter), loc='left')
fig.suptitle('Random Walk', fontsize=20)
ax.set_box_aspect((1, 1, 1))

# グラフを書出
plt.savefig(fname='../figure/RandomWalk/3d_360_xyz_n.png', dpi=250)

plt.show()

# %%

### アニメーションの作成：(座標軸のみ)

# グラフサイズを設定
margin_rate = 0.1
axis_size = np.max([np.abs(x_arr), np.abs(y_arr), np.abs(z_arr)])
axis_size  = np.ceil(axis_size * (1+margin_rate)) # 余白を追加

# グラフオブジェクトを初期化
fig, ax = plt.subplots(figsize=(10, 10), facecolor='white', 
                       subplot_kw={'projection': '3d'})
fig.suptitle('Random Walk', fontsize=20)

# 矢サイズを指定
alr = 1

# 配色の共通化用のカラーマップを作成
cmap = plt.get_cmap("tab10")

# 作図処理を定義
def update(i):
    
    # 前フレームのグラフを初期化
    plt.cla()

    # 3Dランダムウォークを作図
    for s in range(sample_size):
        
        # 現在値を取得
        x = x_arr[s, i]
        y = y_arr[s, i]
        z = z_arr[s, i]

        ax.plot(x_arr[s, :i+1], y_arr[s, :i+1], zs=-axis_size, zdir='z', 
                color=cmap(s), alpha=0.4, linewidth=1, linestyle='dashed') # xy面の軌跡
        ax.plot(y_arr[s, :i+1], z_arr[s, :i+1], zs=-axis_size, zdir='x', 
                color=cmap(s), alpha=0.4, linewidth=1, linestyle='dashed') # yz面の軌跡
        ax.plot(x_arr[s, :i+1], z_arr[s, :i+1], zs=axis_size, zdir='y', 
                color=cmap(s), alpha=0.4, linewidth=1, linestyle='dashed') # xz面の軌跡
        ax.scatter([x, -axis_size, x], 
                   [y, y, axis_size], 
                   [-axis_size, z, z], 
                   s=50, fc='none', ec=cmap(s)) # 面ごとの現在地点
        ax.quiver(x, y, z, 
                  [0, -axis_size-x, 0], [0, 0, axis_size-y], [-axis_size-z, 0, 0], 
                  arrow_length_ratio=0, color=cmap(s), linewidth=1, linestyle='dotted') # 点の目盛線
        ax.plot(x_arr[s, :i+1], y_arr[s, :i+1], z_arr[s, :i+1], 
                color=cmap(s), alpha=0.5) # 軌跡
        ax.scatter(x, y, z, s=50, color=cmap(s)) # 現在地点
    ax.set_xlim(xmin=-axis_size, xmax=axis_size)
    ax.set_ylim(ymin=-axis_size, ymax=axis_size)
    ax.set_zlim(zmin=-axis_size, zmax=axis_size)
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
    filename='../figure/RandomWalk/3d_360_xyz_n.mp4', dpi=250, 
    progress_callback = lambda i, n: print(f'frame: {i} / {n}')
)

# %%


