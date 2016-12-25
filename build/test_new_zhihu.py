import subprocess


def main():
    command = [
            './dlne_main',
            '--dynet-mem 5500',
            '--dynet-seed 12345',
            '--node_list_file ~/zhihu_data/nodes_0.data',
            '~/zhihu_data/nodes_1.data',
            '--edge_list_file ~/zhihu_data/edge_list_0.data',
            '~/zhihu_data/edge_list_1.data',
            '--content_node_file ~/zhihu_data/contents.data',
            '--word_embedding_file ~/DLNE_data/zhihu/zhihu_pre_word_embedding.data',
            '--to_be_saved_index_file_name ~/zhihu_data/labels.data',
            '--eta0 0.3',
            '--eta_decay 0.03',
            '--workers 1',
            '--iterations  100',
            '--batch_size 1000',
            '--save_every_i 10',
            '--report_every_i 100000',
            '--update_epoch_every_i 10000',
            '--negative 15 15 15 15 15',
            '--alpha 1 1 1 1 1',
            '--embedding_method WordAvg',
        ]
    command = ' '.join(command)
    print(command)
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    main()
