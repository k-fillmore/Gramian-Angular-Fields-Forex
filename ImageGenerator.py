import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from pyts.image import GramianAngularField



class GrammianImage:
    def __init__(self, df, window_size, output_dir, fieldtype, quality):
        self.df = df
        self.window_size = window_size
        self.output_dir = output_dir
        self.fieldType = fieldtype
        self.debug_level = 0
        self.quality = quality


    def generateGaf(self):
        values = self.to_numpy()
        # Function Specific parameters
        index_val = self.df.index.max()
        outfile = self.output_dir + str(index_val) + '.jpeg'
        if self.fieldType == 'gasf':
            gaf = GramianAngularField(image_size=self.window_size, method='summation')
        elif self.fieldType == 'gadf':
            gaf = GramianAngularField(image_size=self.window_size, method='difference')
        gaf = gaf.fit_transform(X=values)
        # Generate Image
        fig = plt.figure(figsize=(8, 8))
        grid = ImageGrid(fig, 111,
                         nrows_ncols=(2, 2),
                         axes_pad=0,
                         share_all=True
                         )
        images = [gaf[0], gaf[1], gaf[2], gaf[3]]
        for image, ax in zip(images, grid):
            ax.imshow(image, cmap='rainbow', origin='lower')
            ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)
        ax.cax.toggle_label(False)
        plt.axis('off')
        if self.debug_level == 2:
            plt.show()
        if self.debug_level == 1:
            print(outfile)
        plt.savefig(outfile, pil_kwargs={'optimize': True, 'quality': self.quality})
        plt.close('all')

    def to_numpy(self):
        df = self.df
        close_np = df['close'].to_numpy()
        open_np = df['open'].to_numpy()
        high_np = df['high'].to_numpy()
        low_np = df['low'].to_numpy()
        return [open_np, high_np, low_np, close_np]
