//
//  AVPlayerView.swift
//  SoundWalk
//
//  Created by Marusa Hrobat on 02/02/2021.
//

import SwiftUI
import AVKit

struct AVPlayerView: View {

    // Bind an instance of our new class to the View
    @State var avPlayerWithSpatialization: AVPlayerWithSpatialization
    
    var body: some View {
        VStack {
            Toggle(isOn: $avPlayerWithSpatialization.shouldSpatialize, label: {
                Text("Spatialize Audio")
            }).padding()
            
            VideoPlayer(player: avPlayerWithSpatialization)
                .onAppear() {
                    // Start the player going, otherwise controls don't appear
                    avPlayerWithSpatialization.play()
                }
                .onDisappear() {
                    // Stop the player when the view disappears
                    avPlayerWithSpatialization.pause()
            }
                //.navigationBarBackButtonHidden(true)
                //.navigationBarHidden(true)
                .navigationBarTitle(Text(""), displayMode: .inline)
            
        }
    }
}
