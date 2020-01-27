package de.eliaspr.imagereceiver;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class ImageReceiver {

    public static void main(String[] args) throws IOException {
        DatagramSocket socket = new DatagramSocket(32127);
        byte[] buffer = new byte[1024];
        DatagramPacket packet = new DatagramPacket(buffer, 1024);
        while(true) {
            socket.receive(packet);
            String str = new String(buffer);
            System.out.println(str + " from " + packet.getAddress().toString() + ":" + packet.getPort());
        }
    }

}
