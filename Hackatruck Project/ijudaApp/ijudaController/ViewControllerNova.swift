//
//  ViewControllerNova.swift
//  ijudaApp
//
//  Created by Student on 21/10/19.
//  Copyright © 2019 Student. All rights reserved.
//

import UIKit
import Alamofire

class ViewControllerNova: UIViewController {
    
    @IBOutlet weak var labelbpm: UILabel!
    
    @IBOutlet weak var resultadoLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        makeRequest()
    }
    
    func makeRequest() {
           var last_bpm = ""
           AF.request("https://iotjpbrs13.mybluemix.net/getBPM").responseString { response in
               debugPrint("Response: \(response.value)")
               if response.value != nil {
                   last_bpm = response.value!
                   self.labelbpm.text = last_bpm
                   AF.request("https://iotjpbrs13.mybluemix.net/deletarDados")
               } else {
                   
               }

           }
    }
    
    
    @IBAction func voltarAcao(_ sender: Any) {
        dismiss(animated: false, completion: nil)
    }
    

    @IBAction func backAction2(_ sender: Any) {
        dismiss(animated: false, completion: nil)
    }
    var soma = 0
    var batimentos : Array<Int> = []
    @IBAction func botaoCalibrar(_ sender: Any) {
        
        for _ in 1...5{
            print(self.batimentos)
            sleep(2)
            AF.request("https://iotjpbrs13.mybluemix.net/getBPM").responseString { response in
            debugPrint("Response: \(response.value)")
            if response.value != nil {
                self.soma += Int(response.value!)!
                print(Int(response.value!)!)
                AF.request("https://iotjpbrs13.mybluemix.net/deletarDados")
            } //else {
                
            //}
            
            }
        }
//        var soma = 0
//        for medida in self.batimentos {
//            soma += medida
//        }
//        print(soma)
        print("Ultimo print \(self.soma)")
//        var media = soma / 2
//        self.resultadoLabel.text = String(media)
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
