from molecule_generator import MoleculeGenerator
from property_predictor import PropertyPredictor

def main():
    # 初始化分子生成器和性质预测器
    generator = MoleculeGenerator()
    predictor = PropertyPredictor()
    
    while True:
        # 显示用户选项菜单
        print("\n1. 生成新分子")
        print("2. 预测分子性质")
        print("3. 退出")
        choice = input("请选择操作 (1/2/3): ")
        
        if choice == '1':
            # 生成新分子并显示其SMILES表示
            smiles = generator.generate_molecule()
            print(f"生成的分子SMILES: {smiles}")
        elif choice == '2':
            # 获取用户输入的SMILES并预测其性质
            smiles = input("请输入分子的SMILES表示: ")
            properties = predictor.predict_properties(smiles)
            print("预测的分子性质:")
            for prop, value in properties.items():
                print(f"{prop}: {value}")
        elif choice == '3':
            # 退出程序
            break
        else:
            # 处理无效输入
            print("无效的选择,请重试。")

if __name__ == "__main__":
    main()
    