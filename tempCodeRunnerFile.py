   # def test_truth_table(self):
    #     test = True
    #     for i in range(50):
    #         self.creatNewCase()
    #         self.TT = TT()
    #         self.TT.infer(self.KB, self.query)
    #         result = self.TT.output
    #         flag = False
    #         if "YES" in result:
    #             flag = True
    #         if(flag != self.result):
    #             test = False
    #             print(f"TT fail:{i+1}")
    #             print(self.result)
    #             writeError(self.track,self.query)
    #             break
    #         print(f"TT pass:{i+1}")
    #     print()
    #     self.assertTrue(test)