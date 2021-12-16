from glob import glob
import os

def merge_csv(input_file):
    with open(input_file, encoding='utf-8') as f:
        input_cont = f.readlines()
        print(input_cont)

        file_name = os.path.splitext(os.path.basename(input_file))
        output_all = "./result/opensmile/result_all_add_sa.csv"
        output_con1 = "./result/opensmile/result_condition1_add_sa.csv"
        output_con2 = "./result/opensmile/result_condition2_add_sa.csv"
        output_con3 = "./result/opensmile/result_condition3_add_sa.csv"
        output_con4 = "./result/opensmile/result_condition4_add_sa.csv"
        with open(output_all, 'a', encoding='utf-8') as f:
            f.writelines(input_cont)
            f.write('\n')
        if "condition1" in file_name[0]:
            with open(output_con1, 'a', encoding='utf-8') as f:
                f.writelines(input_cont)
                f.write('\n')
        elif 'condition2' in file_name[0]:
            with open(output_con2, 'a', encoding='utf-8') as f:
                f.writelines(input_cont)
                f.write('\n')
        elif "condition3" in file_name[0]:
            with open(output_con3, 'a', encoding='utf-8') as f:
                f.writelines(input_cont)
                f.write('\n')
        elif "condition4" in file_name[0]:
            with open(output_con4, 'a', encoding='utf-8') as f:
                f.writelines(input_cont)
                f.write('\n')
