package de.eliaspr.imagereceiver;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class ImageReceiver {

    public static void main(String[] args) throws IOException {
        DatagramSocket socket = new DatagramSocket(32127);
        byte[] buffer = new byte[4096];
        DatagramPacket packet = new DatagramPacket(buffer, 4096);
        byte[] imageBuffer = new byte[16 * 1024 * 1024];
        while(true) {
            socket.receive(packet);
            int imageSizeBytes = SerializationUtils.readInt(buffer, 0);
            System.out.println(imageSizeBytes);
        }
    }
// 48645321
}
