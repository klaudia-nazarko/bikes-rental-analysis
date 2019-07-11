import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def round_byTime(df,
                 freq,
                 date_column='start_date',
                 agg={'start_station_id': 'count', 'duration': 'mean'}, other_cols = None):
    """Function groups data by date rounded to given frequency and aggregates it based on definition"""
    
    groupby_cols = [pd.Grouper(key=date_column, freq=freq)]
    if other_cols != None:
        groupby_cols += other_cols
        
    new_df = df.groupby(groupby_cols) \
            .agg(agg) \
            .reset_index() \
            .rename({'start_station_id': 'rentals_count', 'duration': 'avg_duration'}, axis=1)
    
    return(new_df)

def limit_byDates(df, start_date='2015-01-01', end_date='2018-12-31', date_column='start_date'):
    """Function limits data to the selected dates range"""
    return df[(df['start_date']>start_date) & (df['start_date']<end_date)]

def meteo_season(month):
    """Assign meteo season based on month"""
    if month in [3,4,5]:
        return 'spring'
    elif month in [6,7,8]:
        return 'summer'
    elif month in [9,10,11]:
        return 'autumn'
    else:
        return 'winter'

### Visualizations

def dist_byMember(df, column):
    """Plot distribution of a column with division by member type: Member and Casual"""
    title = 'distribution of ' + column + ' by member type'
    
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.distplot(df[df['member_type']=='Member'][column], kde=False, norm_hist=True)
    sns.distplot(df[df['member_type']=='Casual'][column], kde=False, norm_hist=True)
    ax.set_title(title)
    plt.show()
    
def distribution_check(df, column, verbose=True):
    """Plot histogram and boxplot to check distribution. Print values of quantiles"""
    df = df.dropna(axis=0)
    
    gridsize = (1, 3)
    fig = plt.figure(figsize=(16, 5))
    ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=1)
    ax2 = plt.subplot2grid(gridsize, (0, 2))

    sns.distplot(df[column], kde=False, norm_hist=True, ax=ax1)
    sns.boxplot(x=column, data=df, ax=ax2, orient='v')

    plt.tight_layout()
    plt.show()
    
    if verbose:
        for q in [0.25, 0.5, 0.75, 0.95, 0.99]:
            print(q, 'quantile: ', df[column].quantile(q))
        print('max value:', df[column].max())    
    
def draw_overview_plot(x, df, hue=None):
    """Plot bar plot with rentals count and duration divided by a feature defined in arguments"""
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
    palette = sns.husl_palette(10, h=.5)

    sns.barplot(x=x, y='rental_id', hue=hue, data=df, ax=ax1, ci=None, palette=palette)
    ax1.set_title('Total number of rentals')
    ax1.set_ylabel('number of rentals')

    sns.barplot(x=x, y='duration', hue=hue, data=df, ax=ax2, ci=None, palette=palette)
    ax2.set_title('Average rental duration')
    ax2.set_ylabel('rental duration')

    plt.tight_layout()
    plt.show()