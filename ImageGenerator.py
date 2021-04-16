import matplotlib as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import GramianAngularField

class GrammianImage():
    def __init__(self, df, window_size, output_dir, fieldtype):
        self.df = df
        self.window_size = window_size
        self.output_dir = output_dir
        self.fieldType = fieldtype
        self.debug_level = 0
        pass

    def generateGasf(self, values, quality):
        # Function Specific parameters
        index_val = self.df.index.max()
        outfile = self.output_dir + str(index_val) + '.jpeg'
        gasf = GramianAngularField(image_size=100, method='summation')
        X_gasf = gasf.fit_transform(values)
        # Generate Image
        fig = plt.figure(figsize=(8, 8))
        grid = ImageGrid(fig, 111,
                         nrows_ncols=(2, 2),
                         axes_pad=0,
                         share_all=True
                         )
        images = [X_gasf[0], X_gasf[1], X_gasf[2], X_gasf[3]]
        for image, ax in zip(images, grid):
            im = ax.imshow(image, cmap='rainbow', origin='lower')
            ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)
        ax.cax.toggle_label(False)
        plt.axis('off')
        if self.debug_level == 2:
            plt.show()
        if self.debug_level == 1:
            print(outfile)
        plt.savefig(outfile, optimize=True, quality=quality)
        plt.close('all')

    def to_numpy(self):
        df = self.df
        close_np = df['close'].to_numpy()
        open_np = df['open'].to_numpy()
        high_np = df['high'].to_numpy()
        low_np = df['low'].to_numpy()
        return [open_np, high_np, low_np, close_np]
