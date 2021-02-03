//
//  VideoVM.swift
//  SoundWalk
//
//  Created by Marusa Hrobat on 02/02/2021.
//

import SwiftUI
import AVKit


class AVPlayerWithSpatialization: AVPlayer {
    
    var avPlayerItem: AVPlayerItem
    
    // declare shouldSpatialize and change state of avPlayerItem based on this, when the value chnages
    var shouldSpatialize: Bool = true {
        didSet {
            print ("do something on shouldSpatialize changing")
            if shouldSpatialize {
                avPlayerItem.allowedAudioSpatializationFormats = .monoStereoAndMultichannel
            } else {
                avPlayerItem.allowedAudioSpatializationFormats = []
            }
        }
    }
    
    // Initialiser that takes a String URL to play, we also enable Spatialization based on the state of shouldSpatialize
    init(urlToPlay: String) {
        avPlayerItem = AVPlayerItem(url: URL(string: urlToPlay)!)
        if shouldSpatialize {
            avPlayerItem.allowedAudioSpatializationFormats = .monoStereoAndMultichannel
        } else {
            avPlayerItem.allowedAudioSpatializationFormats = []
        }
        // init super class AVPlayer with our AVPlayerItem
        super.init()
        self.replaceCurrentItem(with: avPlayerItem)
    }
    
}

