//
//  VideoModel.swift
//  SoundWalk
//
//  Created by Marusa Hrobat on 02/02/2021.
//

import SwiftUI

struct VideoClip: Identifiable{
    let id = UUID()
    let videoName: String
    let videoUrl: String
}
