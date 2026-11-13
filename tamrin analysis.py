import pandas as pd

class DataVisualizer:
    def init(self, data):
        # داده‌ها را به سری/دیتافریم پانداس تبدیل می‌کنیم
        self.data = pd.Series(data)
        
    def summary(self):
        print("--- Descriptive Statistics ---")
        print(self.data.describe())
        
    def all_plot(self):
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        
        # 1. Line Plot
        axes[0, 0].plot(self.data.values, color='red', linestyle='--')
        axes[0, 0].set_title('Line Plot')
        axes[0, 0].grid(True)
        
        # 2. Scatter Plot
        axes[0, 1].scatter(range(len(self.data)), self.data.values, color='purple')
        axes[0, 1].set_title('Scatter Plot')
        axes[0, 1].grid(True)
        
        # 3. Bar Chart
        axes[0, 2].bar(range(len(self.data)), self.data.values, color='orange')
        axes[0, 2].set_title('Bar Chart')
        
        # 4. Histogram
        axes[1, 0].hist(self.data.values, bins=10, color='green', edgecolor='black')
        axes[1, 0].set_title('Histogram')
        
        # 5. Box Plot
        axes[1, 1].boxplot(self.data.values, patch_artist=True, boxprops=dict(facecolor='lightblue'))
        axes[1, 1].set_title('Box Plot')
        
        # پاک کردن نمودار ششم خالی
        fig.delaxes(axes[1, 2])
        
        plt.tight_layout()
        plt.show()
        
    def all_save(self, prefix='plot'):
        # ذخیره نمودار خطی
        plt.figure()
        plt.plot(self.data.values, color='red')
        plt.title('Line Plot')
        plt.savefig(f'{prefix}_line.png', dpi=300)
        plt.close()
        
        # ذخیره هیستوگرام
        plt.figure()
        plt.hist(self.data.values, bins=10, color='green')
        plt.title('Histogram')
        plt.savefig(f'{prefix}_hist.png', dpi=300)
        plt.close()
        
        print(f"Plots saved with prefix '{prefix}'.")