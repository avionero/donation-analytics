import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.util as ut

def main():

    path_params = ut.load_path_param()
    print(path_params)

    donation_input_path = path_params[0] #"../../input/itcont.txt"
    percentile_input_path = path_params[1] #"../../input/percentile.txt"
    repeat_donors_output_path = path_params[2] #"../../output/repeat_donors.txt"

    #set load data and configurations
    donations_df = ut.load_donations(donation_input_path)
    percentile = int(ut.load_percentile_param(percentile_input_path))

    #eliminate invalid records
    clean_df = ut.eliminate_empty_records(donations_df, 'CMTE_ID', False, False)
    clean_df = ut.eliminate_empty_records(clean_df, 'NAME', False, False)
    clean_df = ut.eliminate_empty_records(clean_df, 'ZIP_CODE', False, False)
    clean_df = ut.eliminate_empty_records(clean_df, 'TRANSACTION_DT', False, False)
    clean_df = ut.eliminate_empty_records(clean_df, 'TRANSACTION_AMT', False, False)
    clean_df = ut.eliminate_empty_records(clean_df, 'OTHER_ID', True, True)

    #set custom index
    dfkey = ut.set_donor_index(clean_df, 'NAME', 'ZIP_CODE')
    dfvc = dfkey.groupby(['key'])
    df_cnt = dfvc['CMTE_ID'].count() >= 2
    df_repeted_donors = dfkey[df_cnt]

    #clean up data
    donnations = ut.clean_record_data(df_repeted_donors, 'ZIP_CODE', 'left', 5)
    donnations = ut.clean_record_data(df_repeted_donors, 'TRANSACTION_DT', 'right', 4)
    donnations.reset_index(drop=True, inplace=True)
    committees = donnations['CMTE_ID'].unique()

    if len(committees) > 0:
        #calculations
        repeat_donors = ut.committees_donor_percentile(committees, donnations, percentile)
        #deliver output
        repeat_donors.to_csv(os.path.abspath(repeat_donors_output_path), sep="|", index=False, header=False)
        print(repeat_donors)

    print('end')

if __name__ == "__main__":
    main()