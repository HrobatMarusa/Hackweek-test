//
//  ContentView.swift
//  SoundWalk
//
//  Created by Marusa Hrobat on 02/02/2021.
//

import SwiftUI


struct ContentView: View {
    @State var spatialization = true
    let videoClips = [
        VideoClip(videoName: "Birdsong 5.1", videoUrl: "http://my-vm.marusatest.bbctest01.uk/hackweek/Birdsong_5.1.mp4"),
        VideoClip(videoName: "Birdsong 7.1", videoUrl: "http://my-vm.marusatest.bbctest01.uk/hackweek/Birdsong_7.1.mp4")
    ]
    
    var body: some View {
            NavigationView {
                VStack {
                    Text("Test files").font(.title).multilineTextAlignment(.center).padding(10).minimumScaleFactor(0.5)
                    Spacer()
                    ForEach(0..<videoClips.count){ videoClip in
                        HStack{
                        NavigationLink(destination: AVPlayerView(avPlayerWithSpatialization: AVPlayerWithSpatialization(urlToPlay: (videoClips[videoClip].videoUrl)))) {
                            HStack{
                            Text(videoClips[videoClip].videoName)
                            }
                        }.buttonStyle(GradientBackgroundStyle())
                        }
                    }
                    Spacer()
                }
            }
    }
}

struct GradientBackgroundStyle: ButtonStyle {

func makeBody(configuration: Self.Configuration) -> some View {
    configuration.label
        .foregroundColor(Color.white)
        .font(.title)
        .minimumScaleFactor(0.5)
        .padding(15)
        .frame(width: 300)
        .background(LinearGradient(gradient: Gradient(colors: [Color.red, Color.yellow]), startPoint: .leading, endPoint: .trailing))
//        .background(LinearGradient(gradient: Gradient(colors: [Color(red:0,green:0,blue:255), Color.orange]), startPoint: .leading, endPoint: .trailing))
        .cornerRadius(15.0)
        .scaleEffect(configuration.isPressed ? 0.9 : 1.0)
}
}

                    
struct ManuView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

